from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phoneNumber = models.IntegerField(default=0)


def createProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.created(user=kwargs['instance'])

    post_save.connect(createProfile, sender=User)