# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-29 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj05app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(max_length=13, unique=True, verbose_name='手机号'),
        ),
    ]
