#coding:utf-8
"""
中文必须添加#coding:utf-8
否则会出现乱码或服务器无法启动等奇怪现象
"""

from __future__ import unicode_literals

from django.db import models

from outis_user.models import OutisUser

# Category of post
class OutisCategory(models.Model):
    name = models.CharField('category_name', default='misc', max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Outis_Category'
        verbose_name_plural = 'Outis_Category'


# Post
class OutisPost(models.Model):
    category_id = models.ForeignKey(OutisCategory, on_delete=models.CASCADE)
    authord_id = models.ForeignKey(OutisUser, on_delete=models.CASCADE)
    title = models.CharField('title', max_length=100)

    # Link is the most importnt content
    # Because we base on link
    link = models.URLField(max_length=200)

    # Description just like a small commnet about the post
    description = models.CharField('description', max_length=500)

    # Tag: User provides several tags
    # format: 'tag1, tag2, tag3'
    tag = models.CharField('tag', max_length=100)

    up = models.IntegerField('up', default=0)
    down = models.IntegerField('down', default=0)
    # Every Post must have an attraction
    # attraction is picture, gif or smal movie
    attraction = models.FileField(upload_to='user/attraction/')
    post_date = models.DateTimeField(auto_now=True)

    comment_number = models.IntegerField(default=0)
    keep_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Outis_Post'
        verbose_name_plural = 'Outis_Post'

# Comments for post
class OutisComment(models.Model):
    user_id = models.ForeignKey(OutisUser, on_delete=models.CASCADE)
    # Comments for every Post
    post_id = models.ForeignKey(OutisPost, on_delete=models.CASCADE)
    content = models.CharField('content', max_length=500)
    post_date = models.DateTimeField(auto_now=True)
    up = models.IntegerField('up', default=0)
    down = models.IntegerField('down', default=0)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Outis_Comment'
        verbose_name_plural = 'Outis_Comment'


