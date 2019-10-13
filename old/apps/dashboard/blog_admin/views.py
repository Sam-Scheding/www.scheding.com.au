from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from apps.custom.mixins import TitleMixin
from api.blog.models import Article #, Tag
from api.blog.forms import CreateArticleForm
from api.account_details.models import UserDetails, Link
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class CreateArticleView(LoginRequiredMixin, TitleMixin, generic.CreateView):
    """
        This is the main view to manage blog articles.
        It contains CreateArticle functionality, but also lists previously written articles
    """

    template_name = 'create_article.html'
    model = Article
    fields = ['title', 'image', 'content']
    success_url = reverse_lazy('accounts:dashboard:blog_admin:create_article')

    # mixin stuff
    page_title = 'Blog'
    active_tab = 'blog'

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Error: Could not create article', extra_tags='danger')
        print(form.errors)
        return HttpResponseRedirect(self.success_url)

    def form_valid(self, form):
        print('request user:', self.request.user)
        user = UserDetails.objects.get(user=self.request.user)
        form.instance.author = "{} {}".format(user.first_name, user.last_name)
        form.instance.user_id = self.request.user.id
        messages.add_message(self.request, messages.SUCCESS, 'Success: Article was created', extra_tags='success')
        return super(CreateArticleView, self).form_valid(form)

    def articles(self):
        """
            In addition to creating articles, it's also useful for the user to see
            articles they've previously written. This method grabs all previously
            written articles that were written by the logged in user.
        """
        try:
            return Article.objects.filter(user=self.request.user)
        except TypeError as e:
            print("User was not logged in")
            return []
        # No need to catch the case where the user hasn't written blogs. It will just return an empty result set


class UpdateArticleView(LoginRequiredMixin, TitleMixin, generic.UpdateView):
    """
        This allows the user to change fields for a single blog article
    """
    model = Article
    context_object_name = 'article'
    template_name = "update_article.html"
    fields = ('title', 'image', 'content', )
    success_url = reverse_lazy('accounts:dashboard:blog_admin:create_article')

    page_title = "Edit Article"
    active_tab = 'blog'

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Error: Could not modify article', extra_tags='danger')
        print(form.errors)
        return HttpResponseRedirect(self.success_url)

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Success: Article was edited', extra_tags='success')
        return super(UpdateArticleView, self).form_valid(form)


# TODO: This should be done with an update view
class ShowHideArticleView(LoginRequiredMixin, generic.View):

    success_url = reverse_lazy('accounts:dashboard:blog_admin:create_article')

    def post(self, request, *args, **kwargs):

        article_id = kwargs.get('pk', None)
        # Check whether the request was valid (the article exists, an id was specified, etc)
        if not article_id:
            messages.add_message(request, messages.ERROR, 'Error: No article with id: {}'.format(article_id), extra_tags='danger')
        else:
            # get the article object corrosponding to 'article_id' and toggle its visibility
            article = Article.objects.get(id=article_id)
            article.visible = not article.visible
            article.save()
            messages.add_message(request, messages.SUCCESS, 'Success: "{}" visibility is now {}'.format(article.title, article.visible), extra_tags='success')
        return redirect(self.success_url)

class DeleteArticleView(LoginRequiredMixin, TitleMixin, generic.DeleteView):
    """
        This deletes the database fields for a single blog article
    """
    model = Article
    page_title = "Delete Article"
    active_tab = 'blog'
    template_name = "delete_article.html"
