# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experienciaacademica',
            name='date_fin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='experienciaacademica',
            name='date_inicio',
            field=models.DateTimeField(),
        ),
    ]