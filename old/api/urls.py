
from django.contrib import admin
from django.urls import path, include
from api.blog import views
from rest_framework import routers
from api.blog import views as blog_views
from api.account_details import views as account_views
from rest_framework.documentation import include_docs_urls


app_name = 'api'

router = routers.DefaultRouter()
router.register('blog/articles', blog_views.ArticleView)
# router.register('blog/tags', blog_views.TagView)
router.register('accounts/details', account_views.UserDetailsView)
router.register('accounts/details/<int:pk>', account_views.UserDetailsView)
router.register('accounts/online_presence', account_views.LinkView)


urlpatterns = [

    path('', include(router.urls)),
    path('events/', include('api.events.urls', namespace='events')),
]
