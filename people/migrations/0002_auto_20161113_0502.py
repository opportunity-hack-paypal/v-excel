# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-12 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastersection',
            name='label',
            field=models.IntegerField(choices=[(1, 'Laundry'), (2, 'Kitchen')]),
        ),
    ]
