# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 19:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 7, 5, 19, 52, 11, 295086, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 7, 5, 19, 52, 11, 296195, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='interest',
            table='interests',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]