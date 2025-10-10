from rest_framework import serializers
from .models import Clientes, Servicos


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'


class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = '__all__'
