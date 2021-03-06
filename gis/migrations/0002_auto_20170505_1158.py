# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('x', models.FloatField(default=0)),
                ('y', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=2000),
        ),
    ]
