from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    # /post/index
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index$', views.IndexView.as_view(), name='index'),
]
