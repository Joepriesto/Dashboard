from __future__ import unicode_literals

from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Process(models.Model):
    """ docstring for Process """
    def __str__(self):
        return str(self.name)
        
    name = models.CharField('name', max_length=25)
    std_hours = models.FloatField(default=0)
    std_resource = models.PositiveIntegerField(default=1)
    std_qty = models.PositiveIntegerField(default=1)

class Batch(models.Model):
    """docstring for Batch"""
    def __str__(self):
        return str(self.lot_number)

    lot_number = models.PositiveIntegerField(default=0)
    start_date = models.DateTimeField('date started', auto_now_add=True)
    start_time = models.DateTimeField('start time', auto_now_add=True)
    duration = models.DurationField('duration', default=timedelta(0))
    process = models.ForeignKey(Process, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return "/timer/%s/" % self.id
# class runPeriod(models.Model):
#     def __str__(self):
#         return self.batch
        

#     batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

