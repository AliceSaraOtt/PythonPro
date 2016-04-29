# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 21:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0010_remove_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='article', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]