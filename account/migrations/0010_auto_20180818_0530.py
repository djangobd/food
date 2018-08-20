# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-18 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20180816_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='employee',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='employee',
            field=models.ManyToManyField(related_name='profile', to='account.Employee'),
        ),
    ]
