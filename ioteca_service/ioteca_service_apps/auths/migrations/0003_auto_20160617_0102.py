# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0002_auto_20160603_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='module',
            field=models.CharField(choices=[('WEB', 'Web informativa'), ('ADMISION', 'Admisión'), ('BACKEND', 'Backend Manager'), ('OTHER', 'Other')], default='BACKEND', max_length=50, verbose_name='module'),
        ),
    ]
