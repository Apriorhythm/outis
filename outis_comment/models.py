# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from outis_user.models import OutisUser
from outis_post.models import OutisPost

# Comments for post
class OutisComment(models.Model):
    user_id = models.ForeignKey(OutisUser, on_delete=models.CASCADE)
    # Comments for every Post
    post_id = models.ForeignKey(OutisPost, on_delete=models.CASCADE)
    reply_to = models.ForeignKey('OutisComment', on_delete=models.CASCADE, default=1)
    content = models.CharField('content', max_length=500)
    post_date = models.DateTimeField(auto_now=True)
    up = models.IntegerField('up', default=0)
    down = models.IntegerField('down', default=0)


    class Meta:
        verbose_name = 'Outis_Comment'
        verbose_name_plural = 'Outis_Comment'



