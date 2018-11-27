from rest_framework import serializers
from .models import Categoria, Producto, Cliente, Mesero, Factura

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('__all__')

class MeseroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mesero
        fields = ('__all__')

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')

class FacturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factura
        fields = ('__all__')