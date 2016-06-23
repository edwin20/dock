from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import ExperienciaAcademica
from ioteca_service_apps.utils.permissions import ModelPermission

from ioteca_service_apps.utils.pagination import ModelPagination


# Create your views here.

class ExperienciaAcademicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExperienciaAcademica

class ExperienciaAcademicaViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = ExperienciaAcademica.objects.all()
    serializer_class = ExperienciaAcademicaSerializer
