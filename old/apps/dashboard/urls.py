from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from apps.dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('blog/', include('apps.dashboard.blog_admin.urls', namespace='blog_admin')),
]


    # path('map/', views.MapView.as_view(), name='map'),
