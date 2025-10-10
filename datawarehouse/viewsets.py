from rest_framework import viewsets, permissions, filters as rest_framework_filters, status
from drf_yasg.utils import swagger_auto_schema
from .models import Clientes, Servicos
from .serializers import ClientesSerializer, ServicosSerializer
from core.filters import DynamicFilterBackend, JQLFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction


class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        DynamicFilterBackend,
        JQLFilterBackend,
        rest_framework_filters.SearchFilter,
        rest_framework_filters.OrderingFilter,
    ]


class ClientesViewSet(BaseModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    search_fields = ['nome_cliente', 'cpf_cnpj']
    ordering_fields = '__all__'

    @swagger_auto_schema(tags=["Clientes"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Clientes"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Clientes"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Clientes"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Clientes"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Clientes"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Clientes"],
        request_body=ClientesSerializer,
        operation_description="Upsert cliente by cpf_cnpj: creates a new Clientes or updates the existing one with the same cpf_cnpj."
    )
    @action(detail=False, methods=['post'], url_path='upsert')
    def upsert(self, request, *args, **kwargs):
        data = request.data
        cpf = data.get('cpf_cnpj')
        if not cpf:
            return Response({'detail': 'cpf_cnpj is required for upsert.'}, status=status.HTTP_400_BAD_REQUEST)

        # Use atomic transaction to avoid race conditions
        with transaction.atomic():
            instance = Clientes.objects.filter(cpf_cnpj=cpf).first()
            print("Instance:", instance)
            if instance is not None:
                serializer = self.get_serializer(instance, data=data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)

            # create new
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ServicosViewSet(BaseModelViewSet):
    queryset = Servicos.objects.all()
    serializer_class = ServicosSerializer
    search_fields = ['nome', 'numero_plano']
    ordering_fields = '__all__'

    @swagger_auto_schema(tags=["Servicos"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Servicos"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Servicos"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Servicos"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Servicos"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Servicos"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Servicos"],
        request_body=ServicosSerializer,
        operation_description="Upsert servico by id_cliente_servico: updates existing Servicos or creates a new one."
    )
    @action(detail=False, methods=['post'], url_path='upsert')
    def upsert(self, request, *args, **kwargs):
        data = request.data
        chave = data.get('id_cliente_servico')
        if chave is None:
            return Response({'detail': 'id_cliente_servico is required for upsert.'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            instance = Servicos.objects.filter(id_cliente_servico=chave).first()
            if instance is not None:
                serializer = self.get_serializer(instance, data=data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
