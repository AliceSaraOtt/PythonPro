from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from auth_models import UserProfile
# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip_addr = models.GenericIPAddressField(unique=True)
    system_type_choices= (
        ('linux','Linux'),
        ('windows','Windows')
    )
    system_type = models.CharField(choices=system_type_choices,max_length=32,default='linux')
    port = models.SmallIntegerField(default=22)
    idc = models.ForeignKey('IDC')
    enabled = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s(%s)' % (self.hostname,self.ip_addr)

class IDC(models.Model):
    name = models.CharField(max_length=32,unique=True)
    memo = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.name

class HostUser(models.Model):
    auth_type_choices = (
        ('ssh-password','SSH/Password'),
        ('ssh-key','SSH/KEY')
    )
    auth_type = models.CharField(choices=auth_type_choices, max_length=32,default='ssh-password')
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=254,blank=True,null=True)

    def __unicode__(self):
        return '(%s)%s ' %(self.auth_type,self.username)


class BindHostToUser(models.Model):
    host = models.ForeignKey(Host)
    host_user = models.ForeignKey(HostUser)
    host_groups  = models.ManyToManyField('HostGroup')

    def get_groups(self):
        return ','.join([g.name for g in self.host_groups.select_related()])

    def __unicode__(self):
        return '%s:%s' %(self.host,self.host_user)

    class Meta:
        unique_together=('host','host_user')

class HostGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)

    def __unicode__(self):
        return self.name






# class IDC(models.Model):
#     name = models.CharField(max_length=20,unique=True)
#
# class Host(models.Model):
#     name = models.CharField(max_length=20)
#     ip = models.GenericIPAddressField()
#     port = models.IntegerField(default=22)
#     system_choices = (('LINUX','linux'),('WINDOWS','windows'),)
#     system = models.CharField(max_length=10,choices=system_choices,default='linux')
#     idc = models.ForeignKey(IDC)
#
# class HostGroup(models.Model):
#     name = models.CharField(max_length=20,unique=True)
#
# class HostUser(models.Model):
#     uname = models.CharField(max_length=30)
#     pwd = models.CharField(max_length=60)
#
# class Department(models.Model):
#     name = models.CharField(max_length=20,unique=True)
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     uname = models.CharField(max_length=20)
#     pwd = models.CharField(max_length=60)
#     dept = models.ManyToManyField(Department)
#     host_group = models.ManyToManyField(HostGroup)
#
# class BindHostToUser(models.Model):
#     host = models.ForeignKey(Host)
#     host_user = models.ForeignKey(HostUser)
#     host_group = models.ManyToManyField(HostGroup)

