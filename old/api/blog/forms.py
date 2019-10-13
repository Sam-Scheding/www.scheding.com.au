from django import forms
from api.blog.models import Article


class CreateArticleForm(forms.ModelForm):

    tags = forms.CharField()
    author = forms.CharField(widget = forms.HiddenInput())

    class Meta:
        model = Article
        fields = '__all__'
