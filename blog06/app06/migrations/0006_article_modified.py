# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 12:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app06', '0005_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 3, 11, 12, 37, 19, 9000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
