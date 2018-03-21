# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WordHuntApp', '0010_merge_20180320_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='competition_rank',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='competitions_won',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(),
        ),
    ]
