# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_article_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('art_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comment', to='app1.article')),
            ],
        ),
    ]
