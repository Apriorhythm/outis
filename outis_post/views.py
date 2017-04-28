from django.views import generic
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

from .models import OutisPost
from .models import OutisCategory



class IndexView(generic.ListView):
    template_name = 'outis_post/index.html'
    context_object_name = 'all_post'

    def get_queryset(self):
        return OutisPost.objects.all()


@login_required
def detail(request, pk):
    post = get_object_or_404(OutisPost, id=pk)
    #post_form = PostForm
    template_name = 'outis_post/detail.html'

    print('##############################')
    print('##############################')

    return render(request, template_name, {
        'object':post,
    #    'post_form':post_form,
    })


class PostCreate(View):
    form_class = PostForm
    template_name = 'outis_post/postcreate.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print('######################################')
            # cleaned (normalized) data
            new_post = OutisPost(
                category_id = form.cleaned_data['category_id'],
                title = form.cleaned_data['title'],
                link = form.cleaned_data['link'],
                description = form.cleaned_data['description'],
                tag = form.cleaned_data['tag'],
                attraction = form.cleaned_data['attraction'],
            )
            print('######################################')
            new_post.authord_id = request.user
            print(new_post.authord_id)
            new_post.save()
            print('######################################')

            return  reverse_lazy('post:index')


class PostUpdate(UpdateView):
    model = OutisPost
    fields = ['title', 'link', 'description', 'tag', 'attraction']
    template_name = 'outis_post/post_form.html'

class PostDelete(DeleteView):
    model = OutisPost
    success_url = reverse_lazy('post:index')



