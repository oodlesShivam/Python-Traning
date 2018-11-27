from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class Post(models.Model):
    today = datetime.now()
    post = models.CharField(max_length=50)
    # created = models.DateTimeField(default=timezone.now)
    # updated = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(today)
    updated = models.DateTimeField(today)
    user = models.ForeignKey(User)