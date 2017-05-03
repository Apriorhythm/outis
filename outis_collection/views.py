# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import OutisPostCollection, OutisUserCollection
from outis_post.models import OutisPost
from outis_user.models import OutisUser


def CollectPost(request, post_pk):
    new_collection = OutisPostCollection(
        user_id = request.user,
        post_id = OutisPost.objects.get(pk=post_pk),
    )
    new_collection.save()

    return HttpResponse("1")

def RemovePost(request, post_pk):
    OutisPostCollection.objects.filter(
        post_id = OutisPost.objects.get(pk=post_pk),
        user_id = request.user,
    ).delete()

    return HttpResponse("1")


def CollectUser(request, user_pk):
    new_collection = OutisUserCollection(
        main_user_id = request.user,
        sub_user_id = OutisUser.objects.get(pk=user_pk),
    )
    new_collection.save()

    return HttpResponse("1")

def RemoveUser(request, user_pk):
    OutisUserCollection.objects.filter(
        main_user_id = request.user,
        sub_user_id = OutisUser.objects.get(pk=user_pk),
    ).delete()

    return HttpResponse("1")









