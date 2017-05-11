# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from outis_user.models import OutisUser
from outis_post.models import OutisPost
from outis_comment.models import OutisComment

class OutisPostVote(models.Model):
    post_id = models.ForeignKey(OutisPost, on_delete=models.CASCADE)
    user_id = models.ForeignKey(OutisUser, on_delete=models.CASCADE)
    ratting = models.BooleanField('rating')
    ratting_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Outis_Post_Vote'
        verbose_name_plural = 'Outis_Post_Vote'



class OutisCommentVote(models.Model):
    comment_id = models.ForeignKey(OutisComment, on_delete=models.CASCADE)
    user_id = models.ForeignKey(OutisUser, on_delete=models.CASCADE)
    ratting = models.BooleanField('rating')
    ratting_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Outis_Comment_Vote'
        verbose_name_plural = 'Outis_Comment_Vote'











