# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.CharField(max_length=100, default='')),
                ('city', models.CharField(max_length=100, default='')),
                ('website', models.URLField(default='')),
                ('phoneNumber', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
