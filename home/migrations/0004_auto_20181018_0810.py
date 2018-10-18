# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20181018_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 28, 8, 10, 21, 706047)),
        ),
    ]
