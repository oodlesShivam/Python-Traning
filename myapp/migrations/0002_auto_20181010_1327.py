# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Online',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('domain', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'onlinee',
            },
        ),
        migrations.RemoveField(
            model_name='dreamreal',
            name='id',
        ),
        migrations.AddField(
            model_name='dreamreal',
            name='auto_increment_id',
            field=models.AutoField(primary_key=True, default=datetime.datetime(2018, 10, 10, 13, 27, 44, 48976, tzinfo=utc), serialize=False),
            preserve_default=False,
        ),
    ]
