from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class IDC(models.Model):
    name = models.CharField(max_length=20,unique=True)

class Host(models.Model):
    name = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()
    port = models.IntegerField(default=22)
    system_choices = (('LINUX','linux'),('WINDOWS','windows'),)
    system = models.CharField(max_length=10,choices=system_choices,default='linux')
    idc = models.ForeignKey(IDC)

class HostGroup(models.Model):
    name = models.CharField(max_length=20,unique=True)

class HostUser(models.Model):
    uname = models.CharField(max_length=30)
    pwd = models.CharField(max_length=60)

class Department(models.Model):
    name = models.CharField(max_length=20,unique=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    uname = models.CharField(max_length=20)
    pwd = models.CharField(max_length=60)
    dept = models.ManyToManyField(Department)
    host_group = models.ManyToManyField(HostGroup)

class BindHostToUser(models.Model):
    host = models.ForeignKey(Host)
    host_user = models.ForeignKey(HostUser)
    host_group = models.ManyToManyField(HostGroup)

