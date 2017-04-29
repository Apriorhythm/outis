from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

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

from .models import OutisPost
from .models import OutisCategory



class IndexView(generic.ListView):
    template_name = 'outis_post/index.html'
    context_object_name = 'all_post'

    def get_queryset(self):
        return OutisPost.objects.all()


class PostDetail(DetailView):
    model = OutisPost
    template_name = 'outis_post/detail.html'


    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PostCreate(View):
    form_class = PostForm
    template_name = 'outis_post/postcreate.html'

    # display a blank form
    @login_required
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    @login_required
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

            return  redirect('/post/index')


class PostUpdate(UpdateView):
    model = OutisPost
    fields = ['title', 'link', 'description', 'tag', 'attraction']
    template_name = 'outis_post/post_form.html'

class PostDelete(DeleteView):
    model = OutisPost
    success_url = reverse_lazy('post:index')



