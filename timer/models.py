from __future__ import unicode_literals

from django.db import models
from datetime import datetime, timedelta

# Create your models here.


class Batch(models.Model):
    """docstring for Batch"""
    def __str__(self):
        return str(self.lot_number)

    lot_number = models.PositiveIntegerField(default=0)
    start_date = models.DateTimeField('date started')
    start_time = models.DateTimeField('start time')
    duration = models.DurationField('duration', default=timedelta(0))
# class runPeriod(models.Model):
#     def __str__(self):
#         return self.batch
        

#     batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
        