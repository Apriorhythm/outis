#coding:utf-8
"""
中文必须添加#coding:utf-8
否则会出现乱码或服务器无法启动等奇怪现象
"""

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import View
from .forms import RegisterForm, LoginForm
from django import forms

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


from outis_collection.models import OutisPostCollection, OutisUserCollection
from outis_post.models import OutisPost
from outis_user.models import OutisUser
from .serializers import OutisUserSerializer


#def login(request):
#    return render(request, 'outis_user/login.html')

#def register(request):
#    return render(request, 'outis_user/register.html')

class RegisterView(View):
    form_class = RegisterForm
    template_name = 'outis_user/register.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('user:profile')


        return render(request, self.template_name, {'form':form})


class LoginView(View):
    form_class = LoginForm
    template_name = 'outis_user/login.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        # cleaned (normalized) data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # returns User object if credentials are correct
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                print(user)
                login(request, user)
                return redirect('user:profile')

        outis_errors = "Sorry, username or password doesn't match"
        return render(request, self.template_name,{'form':form,
        'outis_errors':outis_errors})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('post:index')

class ProfileView(View):
    def get(self, request):
        collect_posts = OutisPost.objects.filter(
            pk__in=request.user.outispostcollection_set.values('post_id')
        )

        return render(request,
            'outis_user/profile.html',
            {'collect_posts': collect_posts},
        )



class PeekUserView(View):
    def get(self, request, user_pk):
        peeked_user = OutisUser.objects.get(pk=user_pk)

        return render(request,
            'outis_user/peek.html',
            {'peeked_user': peeked_user},
        )














