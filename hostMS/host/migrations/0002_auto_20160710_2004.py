# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BindHostToUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64)),
                ('ip_addr', models.GenericIPAddressField(unique=True)),
                ('system_type', models.CharField(choices=[('linux', 'Linux'), ('windows', 'Windows')], default='linux', max_length=32)),
                ('port', models.SmallIntegerField(default=22)),
                ('enabled', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_type', models.CharField(choices=[('ssh-password', 'SSH/Password'), ('ssh-key', 'SSH/KEY')], default='ssh-password', max_length=32)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('memo', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.IDC'),
        ),
        migrations.AddField(
            model_name='bindhosttouser',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.Host'),
        ),
        migrations.AddField(
            model_name='bindhosttouser',
            name='host_groups',
            field=models.ManyToManyField(to='host.HostGroup'),
        ),
        migrations.AddField(
            model_name='bindhosttouser',
            name='host_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.HostUser'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bind_hosts',
            field=models.ManyToManyField(blank=True, to='host.BindHostToUser'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='host_groups',
            field=models.ManyToManyField(blank=True, to='host.HostGroup'),
        ),
        migrations.AlterUniqueTogether(
            name='bindhosttouser',
            unique_together=set([('host', 'host_user')]),
        ),
    ]