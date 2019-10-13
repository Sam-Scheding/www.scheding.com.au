from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from api.events.models import Tag
from api.events.serializers import TagSerializer

class TagView(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
