#coding:utf-8

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
from .forms import PostForm
from django import forms
from django.views.generic import View
from django.utils import timezone
from django.shortcuts import render_to_response

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
#from rest_framework import Status

from pure_pagination.mixins import PaginationMixin

from haystack.forms import SearchForm
from haystack.generic_views import SearchView


from outis_comment.models import OutisComment
from .models import OutisPost, OutisCategory
from .serializers import OutisPostSerializer
from outis_comment.serializers import OutisCommentSerializer

from outis_comment.forms import OutisCommentForm

class FooView(PaginationMixin, ListAPIView):
    def get(self, request):
        queryset = OutisPost.objects.all()
        serializer = OutisPostSerializer(queryset, many=True)
        ordering_fields = ('up_minus_down')

        return Response({
            'all_posts':serializer.data
        })



class GetPosts(PaginationMixin, APIView):
    def get(self, request):
        queryset = OutisPost.objects.all()
        serializer = OutisPostSerializer(queryset, many=True)
        return Response({
            'all_posts':serializer.data
        })



class IndexView(PaginationMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'outis_post/base.html'
    paginate_by = 20

    def get(self, request):
        queryset = OutisPost.objects.all()
        ordering_fields = ('up_minus_down')

        return Response({
            'all_post':queryset,
        })

class MusicView(PaginationMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'outis_post/base.html'
    paginate_by = 20

    def get(self, request):
        queryset = OutisPost.objects.filter(category_id=2)
        return Response({'all_post':queryset})


class VideoView(PaginationMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'outis_post/base.html'
    paginate_by = 20

    def get(self, request):
        queryset = OutisPost.objects.filter(category_id=3)
        return Response({'all_post':queryset})


class MiscView(PaginationMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'outis_post/base.html'
    paginate_by = 20

    def get(self, request):
        queryset = OutisPost.objects.filter(category_id=1)
        return Response({'all_post':queryset})






class PostDetail(DetailView):
    model = OutisPost
    template_name = 'outis_post/detail.html'

    # 新增 form 到 context
    def get_context_data(self, **kwargs):
        kwargs['form'] = OutisCommentForm()
        kwargs['authord_logo'] = self.object.authord_id.logo
        return super(PostDetail, self).get_context_data(**kwargs)


class PostCreate(View):
    form_class = PostForm
    template_name = 'outis_post/postcreate.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        print(form)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # cleaned (normalized) data
            new_post = OutisPost(
                category_id = form.cleaned_data['category_id'],
                title = form.cleaned_data['title'],
                link = form.cleaned_data['link'],
                description = form.cleaned_data['description'],
                tag = form.cleaned_data['tag'],
                attraction = form.cleaned_data['attraction'],
            )
            new_post.authord_id = request.user
            new_post.save()

            return redirect('/post/base')
        else:
            return render(request, self.template_name, {'form':form})


class PostUpdate(UpdateView):
    model = OutisPost
    fields = ['title', 'link', 'description', 'tag', 'attraction']
    template_name = 'outis_post/post_form.html'


class PostDelete(APIView):
    def post(self, request):
        OutisPost.objects.get(pk=request.POST.get('post_id')).delete()

        return Response('1')


class TitleSearch(SearchView):
    def get(self, request):
        keywords = request.GET['q']
        sform = SearchForm(request.GET)
        queryset = sform.search()
        template_name = 'outis_post/base.html'

        return render_to_response(template_name, {'all_post':queryset})


"""
def titleSearch(request):
    keywords = request.GET['q']
    sform = SearchForm(request.GET)
    queryset = sform.search()
    template_name = 'outis_post/foo.html'

    print('SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')

    print('SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')

    return render_to_response(template_name, {'all_post':queryset})
"""

class AllMyPost(PaginationMixin, APIView):
    def get(self, request):
        posts = OutisPost.objects.filter(authord_id=request.user)
        serializer = OutisPostSerializer(posts, many=True)

        return Response(serializer.data)



