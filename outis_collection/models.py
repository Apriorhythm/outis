# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from outis_post.models import OutisPost
from outis_user.models import OutisUser

class OutisPostCollection(models.Model):
    user_id = models.ForeignKey(OutisUser, on_delete=models.CASCADE)
    post_id = models.ForeignKey(OutisPost, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Outis_Post_Collection'
        verbose_name_plural = 'Outis_Post_Collection'

    def __str__(self):
        return self.id


class OutisUserCollection(models.Model):
    main_user_id = models.ForeignKey(OutisUser, verbose_name='main_user_id',
        related_name='main_user_id', on_delete=models.CASCADE)
    sub_user_id = models.ForeignKey(OutisUser, verbose_name='sub_user_id',
        related_name='sub_user_id')
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Outis_User_Collection'
        verbose_name_plural = 'Outis_User_Collection'

    def __str__(self):
        return self.id



