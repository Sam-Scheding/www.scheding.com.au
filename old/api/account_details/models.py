from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):

    name = models.CharField(max_length=64)
    url = models.URLField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserDetails(models.Model):

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to='users/img', default='users/img/default_profile_pic.png')
    bio = models.TextField(default="")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
