# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WordHuntApp', '0014_auto_20180322_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='currently_participates',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='rank',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
    ]