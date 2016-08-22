from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Batch(models.Model):
    """docstring for Batch"""
    def __str__(self):
        return self.lot_number

    lot_number = models.PositiveIntegerField(default=0)
    start_date = models.DateTimeField('date started')

class runPeriod(models.Model):
    def __str__(self):
        return self.batch
        
    start_time = models.DateTimeField('start time')
    time_taken = models.DurationField(default=0)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
        