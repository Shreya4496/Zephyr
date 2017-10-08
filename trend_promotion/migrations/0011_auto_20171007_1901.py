# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend_promotion', '0010_potentialoffers_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potentialoffers',
            name='arrival_time',
            field=models.DateTimeField(max_length=50),
        ),
        migrations.AlterField(
            model_name='potentialoffers',
            name='counter',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='potentialoffers',
            name='departure_time',
            field=models.DateTimeField(max_length=50),
        ),
    ]
