from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Investigacion
from ioteca_service_apps.utils.permissions import ModelPermission

from ioteca_service_apps.utils.pagination import ModelPagination


# Create your views here.

class InvestigacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Investigacion



class InvestigacionViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = Investigacion.objects.all()
    serializer_class = InvestigacionSerializer
