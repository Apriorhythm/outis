from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'post'

urlpatterns = [
    url(r'^foo$', views.FooView.as_view(), name='foo'),

    # /post/index
    url(r'^$', views.IndexView.as_view(), name='base'),
    url(r'^index$', views.IndexView.as_view(), name='index'),
    url(r'^music$', views.MusicView.as_view(), name='music'),
    url(r'^video$', views.VideoView.as_view(), name='video'),
    url(r'^misc$', views.MiscView.as_view(), name='misc'),

    # /post/detail/1234/
    url(r'^detail/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='detail'),

    # /post/add/
    url(r'^add$', login_required(views.PostCreate.as_view()), name='post-add'),

    # /music/netease/25/
    #url(r'^(?P<pk>[0-9]+)/$', views.PostUpdate.as_view(), name='post-update'),

    # /post/delete
    url(r'^delete$', login_required(views.PostDelete.as_view()), name='post-delete'),

    url(r'^titleSearch/', views.TitleSearch.as_view(), name='titleSearch'),

    url(r'^allMyPost$', views.AllMyPost.as_view(), name='allMyPost'),


]

