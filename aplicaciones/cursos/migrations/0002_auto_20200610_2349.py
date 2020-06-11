# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-06-10 23:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='autores',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curso',
            name='sobre_curso',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
