from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'events'

router = routers.DefaultRouter()
router.register('', views.EventsAPIView)

urlpatterns = [
    path('', views.EventsView.as_view()),
    path('json', include(router.urls)),
]
