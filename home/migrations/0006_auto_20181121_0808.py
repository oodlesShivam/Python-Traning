# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20181119_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 11, 21, 8, 8, 14, 445910)),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 11, 21, 8, 8, 14, 445910)),
        ),
    ]
