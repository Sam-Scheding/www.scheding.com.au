from api.blog.models import Article #, Tag
from api.blog.serializers import ArticleSerializer #, TagSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

# /api/blog/articles
class ArticleView(viewsets.ModelViewSet):

    queryset = Article.objects.filter(visible=True)
    serializer_class = ArticleSerializer

    def partial_update(self, request, pk=None):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.save()
        serializer.is_valid(raise_exception=True)
        print('Is this running\n\n\n\n\n\n')
        return Response(serializer.data)

# /api/blog/tags
# class TagView(viewsets.ModelViewSet):
#
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
