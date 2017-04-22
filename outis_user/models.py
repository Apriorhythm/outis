#coding:utf-8
"""
中文必须添加#coding:utf-8
否则会出现乱码或服务器无法启动等奇怪现象
"""


from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class OutisUser(AbstractUser):
    heat = models.SmallIntegerField('heat', default=1)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Outis User'
        verbose_name_plural = 'Outis User'

