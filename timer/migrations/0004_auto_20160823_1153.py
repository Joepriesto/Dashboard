# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 10:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0003_auto_20160823_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 23, 11, 53, 43, 190000), verbose_name='start time'),
        ),
    ]
