# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-06-10 22:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito_compra',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fecha_compra', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('cursos', models.ManyToManyField(blank=True, to='cursos.Curso')),
            ],
        ),
    ]
