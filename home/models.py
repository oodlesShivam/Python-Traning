from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
