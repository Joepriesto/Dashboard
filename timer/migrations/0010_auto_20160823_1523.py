# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 14:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0009_auto_20160823_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 23, 14, 23, 5, 551000), verbose_name='start time'),
        ),
    ]
