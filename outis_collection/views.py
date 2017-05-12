# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from pure_pagination.mixins import PaginationMixin

from .models import OutisPostCollection, OutisUserCollection
from outis_post.models import OutisPost
from outis_post.serializers import OutisPostSerializer
from outis_user.models import OutisUser
from outis_user.serializers import OutisUserSerializer


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


class personalPostCollection(PaginationMixin, APIView):

    def get(self, request):
        posts = OutisPost.objects.filter(
            pk__in=request.user.outispostcollection_set.values('post_id')
        )
        serializer = OutisPostSerializer(posts, many=True)

        return Response(serializer.data)


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



class personalUserCollection(PaginationMixin, APIView):

    def get(self, request):
        users = OutisUser.objects.filter(
            pk__in=OutisUserCollection.objects.filter(
                main_user_id=request.user).values('main_user_id')
        )
        serializer = OutisUserSerializer(users, many=True)

        return Response(serializer.data)








