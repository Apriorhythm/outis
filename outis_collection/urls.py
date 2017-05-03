from django.conf.urls import url
from . import views

app_name = 'collection'

urlpatterns = [
    url(r'^post/(?P<post_pk>[0-9]+)/collect$', views.CollectPost, name='collect_post'),
    url(r'^post/(?P<post_pk>[0-9]+)/remove$', views.RemovePost, name='remove_post'),

    url(r'^user/(?P<user_pk>[0-9a-f-]+)/collect$', views.CollectUser, name='collect_post'),
    url(r'^user/(?P<user_pk>[0-9a-f-]+)/remove$', views.RemoveUser, name='remove_post'),
]
