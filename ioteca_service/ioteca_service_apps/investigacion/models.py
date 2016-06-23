from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Investigacion(models.Model):

    editorial = models.CharField(max_length=100)
    medio_publicacion = models.CharField(max_length=100)
    titulo_publicacion = models.CharField(max_length=100)
    isbn = models.IntegerField()
    numero_paginas = models.IntegerField()
    fecha_publicacion = models.DateField()


    class Meta:
        verbose_name = "Investigacion"
        verbose_name_plural = "Investigaciones"

    def __str__(self):
        return self.titulo_publicacion
