# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


from outis_post.models import OutisPost
from outis_comment.models import OutisComment
from .models import OutisPostVote, OutisCommentVote

class VotePost(APIView):
    def post(self, request, post_pk):
        up_or_down = request.POST.get('ratting')
        ratting = False
        if up_or_down == 'up':
            ratting = True

        try:
            existing_vote = OutisPostVote.objects.get(
                user_id=request.user,
                post_id=post_pk,
            )
            if existing_vote.ratting == ratting:
                existing_vote.delete()
            else:
                existing_vote.ratting = not existing_vote.ratting
                existing_vote.save()
        except OutisPostVote.DoesNotExist:
            new_vote = OutisPostVote(
                post_id = OutisPost.objects.get(pk=post_pk),
                user_id = request.user,
                ratting = ratting,
            )
            new_vote.save()

        isOK = 'OK'
        thePost = OutisPost.objects.get(pk=post_pk)
        up = thePost.outispostvote_set.filter(ratting=True).count()
        down = thePost.outispostvote_set.filter(ratting=False).count()

        return Response({
            'isOK':isOK,
            'up':up,
            'down':down,
        })


@login_required
def VoteComment(request, comment_pk):
    up_or_down = request.POST.get('ratting')
    ratting = False
    if up_or_down == 'up':
        ratting = True

    try:
        existing_vote = OutisCommentVote.objects.get(user_id=request.user)
        if existing_vote.ratting == ratting:
            existing_vote.delete()
        else:
            existing_vote.ratting = not existing_vote.ratting
            existing_vote.save()
    except OutisCommentVote.DoesNotExist:
        new_vote = OutisCommentVote(
            comment_id = OutisComment.objects.get(pk=comment_pk),
            user_id = request.user,
            ratting = ratting,
        )
        new_vote.save()

    return HttpResponse('OK')




