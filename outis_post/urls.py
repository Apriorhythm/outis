from django.conf.urls import url
from . import views

app_name = 'post'

urlpatterns = [
    url(r'^foo$', views.FooView.as_view(), name='foo'),

    # /post/index
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index$', views.IndexView.as_view(), name='index'),
    url(r'^music$', views.MusicView.as_view(), name='music'),
    url(r'^video$', views.VideoView.as_view(), name='video'),
    url(r'^misc$', views.MiscView.as_view(), name='misc'),

    # /post/detail/1234/
    url(r'^detail/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='detail'),

    # /post/add/
    url(r'^add$', views.PostCreate.as_view(), name='post-add'),

    # /music/netease/25/
    url(r'^(?P<pk>[0-9]+)/$', views.PostUpdate.as_view(),
    name='post-update'),

    # /post/25/delete
    url(r'^(?P<pk>[0-9]+)/delete$', views.PostDelete.as_view(),
    name='post-delete'),

    url(r'^titleSearch/', views.titleSearch, name='titleSearch'),



]

