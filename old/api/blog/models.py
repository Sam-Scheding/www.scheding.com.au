from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# class Tag(models.Model):
#
#     name = models.CharField(max_length=32, primary_key=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         ordering = ('name',)

class Article(models.Model):

    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, help_text='Readable name to be displayed for articles.')
    content = RichTextUploadingField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/img', default='articles/img/default_blog_img.png', help_text='Preview Image for the article.')
    # tags = models.ManyToManyField(Tag, help_text="Space seperated, e.g. (javascript django ).")
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('date', 'id')
