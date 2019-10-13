from django.db import models
from ..events.models import Event

class Link(models.Model):

    title = models.CharField(max_length=256)
    href = models.CharField(max_length=256)
    model = models.ForeignKey(Event, on_delete=models.CASCADE)

class Tag(models.Model):
    title = models.CharField(max_length=128)
