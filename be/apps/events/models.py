from django.db import models

class Event(models.Model):

    title = models.CharField(max_length=256)
    cron = models.CharField(max_length=64)
    duration = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=2048, blank=True)
    img = models.CharField(max_length=512, blank=True)
    url = models.URLField(max_length=256, blank=True)
    location = models.CharField(max_length=512, blank=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title
