# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20181010_1327'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Online',
        ),
        migrations.RemoveField(
            model_name='dreamreal',
            name='auto_increment_id',
        ),
        migrations.AddField(
            model_name='dreamreal',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, default=datetime.datetime(2018, 10, 10, 13, 36, 25, 788041, tzinfo=utc), serialize=False, auto_created=True),
            preserve_default=False,
        ),
    ]
