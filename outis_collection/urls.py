from django.conf.urls import url
from . import views

app_name = 'collection'

urlpatterns = [
    url(r'^post/(?P<post_pk>[0-9]+)/collect$', views.CollectPost, name='collect_post'),
    url(r'^post/remove$', views.RemovePost.as_view(), name='remove_post'),
    url(r'^post/personalPostCollection$',
        views.personalPostCollection.as_view(), name='personal_post_collection'),

    url(r'^user/(?P<user_pk>[0-9a-f-]+)/collect$', views.CollectUser, name='collect_post'),
    url(r'^user/remove$', views.RemoveUser.as_view(), name='remove_user'),
    url(r'^user/personalUserCollection/$',
        views.personalUserCollection.as_view(), name='personal_user_collection'),
]
