# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 00:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0002_auto_20160705_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 7, 6, 0, 4, 42, 233983, tzinfo=utc)),
        ),
    ]
