# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-21 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180421_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermeal',
            name='thali',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
