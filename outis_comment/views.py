# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from outis_post.forms import PostForm
from django import forms
from django.views.generic import View
from django.utils import timezone
from django.shortcuts import render_to_response

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from pure_pagination.mixins import PaginationMixin

from haystack.forms import SearchForm

from outis_post.models import OutisPost, OutisCategory
from .models import OutisComment

from .serializers import OutisCommentSerializer

from .forms import OutisCommentForm



@login_required
def PostPostComment(request, post_pk):

    post = get_object_or_404(OutisPost, pk=post_pk)

    if request.method == 'POST':
        form = OutisCommentForm(request.POST)

        if form.is_valid():
            comment = OutisComment(content = form.cleaned_data['content'])
            comment.user_id = request.user
            comment.post_id = post
            comment.save()

            return redirect('post:index')
        else:
            # 注意这里我们用到了 post.comment_set.all() 方法
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论
            # 因为 Post 和 Comment 是 ForeignKey 关联的
            # 因此使用 post.comment_set.all() 反向查询全部评论
            # 正向查询就直接是 comment.post
            return render(request, 'outis_post/detail.html', {
                'form': form,
                'post': post,
                'comment_list': post.outiscomment_set.all(),
            })
    return render(request, 'outis_post/detail.html', {
        'form': form,
        'post': post,
        'comment_list': post.outiscomment_set.all(),
    })


class GetPostComment(PaginationMixin, APIView):

    def get(self, request, post_pk):
        comments = OutisComment.objects.filter(post_id=post_pk)
        serializer = OutisCommentSerializer(comments, many=True)

        return Response(serializer.data)


