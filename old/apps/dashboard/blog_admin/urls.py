from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import re_path, path, include
from apps.dashboard.blog_admin import views

app_name = 'blog_admin'

urlpatterns = [
    path('', views.CreateArticleView.as_view(), name='create_article'),
    path('update/<int:pk>', views.UpdateArticleView.as_view(), name='update_article'),
    path('visible/<int:pk>', views.ShowHideArticleView.as_view(), name='show_hide_article'),


]
