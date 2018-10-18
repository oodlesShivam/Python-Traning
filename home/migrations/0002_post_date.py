# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 6, 57, 6, 462751, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
