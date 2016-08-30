from django.contrib import admin

# Register your models here.
from .models import Batch, Process

admin.site.register(Batch)
admin.site.register(Process)
