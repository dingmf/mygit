# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-30 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj05app', '0002_auto_20180829_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='icon',
            field=models.ImageField(null=True, upload_to='icons'),
        ),
    ]
