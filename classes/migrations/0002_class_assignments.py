# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='assignments',
            field=models.ManyToManyField(to='assignments.Assignment'),
        ),
    ]
