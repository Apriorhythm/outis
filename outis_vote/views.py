# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from outis_post.models import OutisPost
from outis_comment.models import OutisComment
from .models import OutisPostVote, OutisCommentVote

@login_required
def VotePost(request, post_pk):
    up_or_down = request.POST.get('ratting')
    ratting = False
    if up_or_down == 'up':
        ratting = True

    try:
        existing_vote = OutisPostVote.objects.get(user_id=request.user)
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

    return HttpResponse('OK')


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




