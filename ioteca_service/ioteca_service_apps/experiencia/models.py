from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ExperienciaAcademica(models.Model):

    certificado = models.CharField(max_length=100)
    resolucion = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    date_inicio = models.DateField()
    date_fin = models.DateField()

    class Meta:
        verbose_name = "Experiencia Academica"
        verbose_name_plural = "Experiencias Academicas"

    def __str__(self):
        return self.institucion
