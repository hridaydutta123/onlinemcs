# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 20:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mcs', '0005_unstructuredtxt_sentimentpolarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='Ttl',
            field=models.CharField(default=datetime.datetime(2016, 2, 23, 20, 12, 53, 242574, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]