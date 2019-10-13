from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from apps.events.serializers import EventSerializer
from rest_framework import viewsets

import croniter
import datetime

from .models import Event

class EventsAPIView(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Create your views here.
class EventsView(generic.TemplateView):

    template_name = "index.html"

    def events(self, *args, **kwargs):
        today = datetime.datetime.today()
        next_week = today + datetime.timedelta(days=7)
        events = []
        event_objs = Event.objects.all()

        for event in event_objs:
            cron = croniter.croniter(event.start, today)
            occurrance = cron.get_next(datetime.datetime)

            while occurrance < next_week:
                occurrance = cron.get_next(datetime.datetime)
                # event.datetime = occurrance
                # events += event
        return event_objs
