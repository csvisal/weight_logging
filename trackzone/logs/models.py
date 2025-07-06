from django.db import models

class LogEntry(models.Model):
        name = models.CharField(max_length=50, blank=True)
        weight = models.FloatField()
        note = models.TextField(blank=True)
        date = models.DateField(auto_now_add=True)
        
# Create your models here.
