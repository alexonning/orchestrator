from django_filters import rest_framework as filters
from django.db import models
from django.db.models import JSONField

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


