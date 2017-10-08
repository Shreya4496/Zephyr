# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-06 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trend_promotion', '0006_auto_20171006_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='pref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('window', models.CharField(max_length=50)),
                ('recliner', models.CharField(max_length=50)),
                ('leg', models.CharField(max_length=50)),
                ('neck', models.CharField(max_length=50)),
                ('cushion', models.CharField(max_length=50)),
                ('veg', models.CharField(max_length=50)),
                ('nonveg', models.CharField(max_length=50)),
                ('special_pref', models.CharField(max_length=500)),
                ('payment', models.CharField(max_length=50)),
                ('pnr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trend_promotion.FlightStatus')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trend_promotion.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='pnr',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='Preferences',
        ),
    ]
