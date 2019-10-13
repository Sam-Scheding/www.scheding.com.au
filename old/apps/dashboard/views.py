from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from apps.custom.mixins import TitleMixin
from api.blog.models import Article
from api.blog.forms import CreateArticleForm
from api.account_details.models import UserDetails, Link

class DashboardView(LoginRequiredMixin, TitleMixin, generic.TemplateView):

    page_title = 'Dashboard'
    active_tab = 'dashboard'
    template_name = 'registration/dashboard.html'


class ProfileView(LoginRequiredMixin, TitleMixin, generic.TemplateView):
    page_title = 'Profile'
    active_tab = 'profile'
    template_name = 'registration/profile.html'

    def me(self):
        try:
            return UserDetails.objects.get(user_id=self.request.user)
        except TypeError as e:
            return None

    def links(self):
        try:
            return Link.objects.filter(user=self.request.user)
        except TypeError as e:
            return []


# BlogView is in the subapp 'blog_admin'
