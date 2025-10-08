from django_filters import rest_framework as filters
from rest_framework.filters import BaseFilterBackend
from django.db import models
from django.db.models import JSONField
from django.db.models import Q
import re
from typing import List, Tuple, Any

class DynamicFilterBackend(filters.DjangoFilterBackend):
    def get_filterset_class(self, view, queryset=None):
        """
        Return a custom filterset class for dynamic filtering
        """
        meta_class = type('Meta', (), {
            'model': queryset.model if queryset is not None else None,
            'fields': '__all__',
            'filter_overrides': {
                JSONField: {
                    'filter_class': filters.CharFilter,
                    'extra': lambda f: {
                        'lookup_expr': 'icontains',
                    }
                },
                models.DateTimeField: {
                    'filter_class': filters.DateTimeFilter,
                    'extra': lambda f: {
                        'lookup_expr': ['exact', 'lt', 'lte', 'gt', 'gte']
                    }
                }
            }
        })
        
        filterset_class = type(
            f'{queryset.model.__name__}FilterSet' if queryset is not None else 'DefaultFilterSet',
            (filters.FilterSet,),
            {'Meta': meta_class}
        )
        
        return filterset_class


class JQLFilterBackend(BaseFilterBackend):
    """A lightweight JQL-like parser that supports a small subset of expressions.

    Supported features:
    - Comparisons: =, !=, ~ (contains), >, <, >=, <=
    - IN operator with parenthesized list: field IN (a,b)
    - Logical operators: AND, OR
    - Parentheses for grouping
    - ORDER BY <field> [ASC|DESC]

    Usage: provide a `jql` query parameter, e.g.
      ?jql=automation__project_name = "MyProj" AND status != "completed" ORDER BY created_at DESC
    """

    _token_re = re.compile(r'"[^"]*"|\'[^\']*\'|\(|\)|!=|>=|<=|=|~|>|<|,|\bIN\b|\bAND\b|\bOR\b|[^\s()=~<>!,]+', re.I)

    def filter_queryset(self, request, queryset, view):
        raw = request.GET.get('jql')
        if not raw:
            return queryset

        # split ORDER BY if present
        parts = re.split(r'\bORDER\s+BY\b', raw, flags=re.I)
        expr = parts[0].strip()
        order_clause = parts[1].strip() if len(parts) > 1 else None

        try:
            tokens = [t for t in self._token_re.findall(expr) if t and not t.isspace()]
            q_obj, _ = self._parse_or(tokens, 0)
            if q_obj is not None:
                queryset = queryset.filter(q_obj)
        except Exception:
            # If parsing fails, ignore JQL rather than raise, to avoid breaking endpoints
            return queryset

        if order_clause:
            # simple order parser: support single field and optional ASC/DESC
            parts = order_clause.split()
            field = parts[0]
            direction = parts[1].upper() if len(parts) > 1 else 'ASC'
            if direction == 'DESC':
                queryset = queryset.order_by(f'-{field}')
            else:
                queryset = queryset.order_by(field)

        return queryset

    # Parser utilities: recursive descent
    def _parse_or(self, tokens: List[str], i: int) -> Tuple[Q, int]:
        left, i = self._parse_and(tokens, i)
        while i < len(tokens) and tokens[i].upper() == 'OR':
            i += 1
            right, i = self._parse_and(tokens, i)
            left = left | right
        return left, i

    def _parse_and(self, tokens: List[str], i: int) -> Tuple[Q, int]:
        left, i = self._parse_term(tokens, i)
        while i < len(tokens) and tokens[i].upper() == 'AND':
            i += 1
            right, i = self._parse_term(tokens, i)
            left = left & right
        return left, i

    def _parse_term(self, tokens: List[str], i: int) -> Tuple[Q, int]:
        tok = tokens[i]
        if tok == '(':
            i += 1
            q_obj, i = self._parse_or(tokens, i)
            # expect ')'
            if i < len(tokens) and tokens[i] == ')':
                i += 1
            return q_obj, i

        # otherwise expect: field operator value
        field = tokens[i]
        i += 1
        if i >= len(tokens):
            raise ValueError('Expected operator after field')
        op = tokens[i]
        i += 1

        if op.upper() == 'IN':
            # expect ( value (, value)* )
            if tokens[i] != '(':
                raise ValueError('Expected ( after IN')
            i += 1
            values = []
            while i < len(tokens) and tokens[i] != ')':
                if tokens[i] == ',':
                    i += 1
                    continue
                values.append(self._parse_value(tokens[i]))
                i += 1
            if i < len(tokens) and tokens[i] == ')':
                i += 1
            q_obj = Q(**{f"{field}__in": values})
            return q_obj, i

        # normal comparison
        if i > len(tokens):
            raise ValueError('Expected value after operator')
        value = self._parse_value(tokens[i])
        i += 1

        # map operator to lookup
        lookup = None
        negate = False
        if op == '=':
            lookup = 'exact'
        elif op == '!=':
            lookup = 'exact'
            negate = True
        elif op == '~':
            lookup = 'icontains'
        elif op == '>':
            lookup = 'gt'
        elif op == '<':
            lookup = 'lt'
        elif op == '>=':
            lookup = 'gte'
        elif op == '<=':
            lookup = 'lte'
        else:
            raise ValueError(f'Unsupported operator: {op}')

        q = Q(**{f"{field}__{lookup}": value})
        if negate:
            q = ~q
        return q, i

    def _parse_value(self, token: str) -> Any:
        # strip quotes
        if (token.startswith('"') and token.endswith('"')) or (token.startswith("'") and token.endswith("'")):
            return token[1:-1]
        low = token.lower()
        if low == 'true':
            return True
        if low == 'false':
            return False
        # number?
        try:
            if '.' in token:
                return float(token)
            return int(token)
        except Exception:
            return token


