from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import CategoriaDocente, RegimenDocente
from ioteca_service_apps.utils.permissions import ModelPermission

from ioteca_service_apps.utils.pagination import ModelPagination

# Create your views here.

class CategoriaDocenteSerializer(serializers.ModelSerializer):
#    tipo_categoria = serializers.SerializerMethodField()

    class Meta:
        model = CategoriaDocente

#    def get_tipo_categoria(self, obj):
#        return obj.get_tipo_categoria_display()

class CategoriaDocenteViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = CategoriaDocente.objects.all()
    serializer_class = CategoriaDocenteSerializer
#    permission_classes = [ModelPermission, ]

class RegimenDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegimenDocente

class RegimenDocenteViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = RegimenDocente.objects.all()
    serializer_class = RegimenDocenteSerializer
