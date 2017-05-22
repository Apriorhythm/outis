# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import OutisPost
from outis_vote.models import OutisPostVote


class OutisPostSerializer(serializers.ModelSerializer):

    authord = serializers.SerializerMethodField()
    authord_logo = serializers.SerializerMethodField()
    up = serializers.SerializerMethodField()
    down = serializers.SerializerMethodField()
    up_minus_down = serializers.SerializerMethodField()


    class Meta:
        model = OutisPost
        fields = ('id', 'category_id', 'authord_id', 'authord', 'authord_logo', 'title', 'link', 'description', 'tag',
            'attraction', 'up', 'down', 'up_minus_down', 'post_date')

    def get_authord(self, post):
        return post.authord_id.username

    def get_authord_logo(self, post):
        return post.authord_id.logo.url


    def get_up(self, post):
        return post.outispostvote_set.filter(ratting=True).count()

    def get_down(self, post):
        return post.outispostvote_set.filter(ratting=False).count()

    def get_up_minus_down(self, post):
        up = post.outispostvote_set.filter(ratting=True).count()
        down = post.outispostvote_set.filter(ratting=False).count()

        return up - down


