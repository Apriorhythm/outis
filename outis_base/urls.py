"""
This is user app
"""
from django.conf.urls import url
from . import views

# My Urls

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),

]
