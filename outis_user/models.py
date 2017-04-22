#coding:utf-8
"""
中文必须添加#coding:utf-8
否则会出现乱码或服务器无法启动等奇怪现象
"""

from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class OutisUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    heat = models.SmallIntegerField('heat', default=1)
    logo = models.ImageField()


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Outis_User'
        verbose_name_plural = 'Outis_User'

