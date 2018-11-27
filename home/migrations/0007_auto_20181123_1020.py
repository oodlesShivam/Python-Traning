# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20181121_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 11, 23, 10, 20, 33, 890922)),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 11, 23, 10, 20, 33, 890922)),
        ),
    ]
