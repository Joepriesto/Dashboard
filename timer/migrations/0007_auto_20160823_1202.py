# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 11:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0006_auto_20160823_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 23, 12, 2, 10, 575000), verbose_name='start time'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='time_taken',
            field=models.DurationField(),
        ),
    ]
