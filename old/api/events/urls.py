from django.contrib import admin
from django.urls import path, include
from api.blog import views
from rest_framework import routers
from api.events import views
from api.account_details import views as account_views
from rest_framework.documentation import include_docs_urls


app_name = 'events'

router = routers.DefaultRouter()
router.register('tags', views.TagView)

urlpatterns = [

    path('', include(router.urls)),

]
