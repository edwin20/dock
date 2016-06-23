from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CategoriaDocente(models.Model):

    DOCENTE_CATEGORIA=(
    ('AX', 'Auxiliar'),
    ('P', 'Principal'),
    ('AS', 'Asociado'),
    )

    catedra=models.CharField(max_length=100)
    institucion=models.CharField(max_length=100)
    lugar=models.CharField(max_length=100)
    tipo_categoria=models.CharField(max_length=2, choices=DOCENTE_CATEGORIA)
    date_inicio = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoria Docente"
        verbose_name_plural = "Categoria Docentes"

    def __str__(self):
        return self.catedra

class RegimenDocente(models.Model):
    REGIMEN_DOCENTE=(
    ('DX', 'Dedicacion Exclusiva'),
    ('TC', 'Tiempo Completo'),
    ('TP', 'Tiempo Parcial'),
    ('PA', 'Pasantia'),
    ('PC', 'Practicante'),
    )
    tipo_regimen=models.CharField(max_length=2, choices=REGIMEN_DOCENTE)

    class Meta:
        verbose_name = "Regimen Docente"
        verbose_name_plural = "Regimen Docentes"

    def __str__(self):
        return u"%s" % (self.get_tipo_regimen_display())
