# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import OutisPostComment


class OutisPostCommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    user_logo = serializers.SerializerMethodField()

    class Meta:
        model = OutisPostComment
        fields = ('id', 'post_id', 'user_id', 'username', 'user_logo', 'content', 'post_date', 'up', 'down')

    def get_username(self, comment):
        return comment.user_id.username

    def get_user_logo(self, comment):
        return comment.user_id.logo.url

