from django.conf.urls import url
from . import views

app_name = 'comment'

urlpatterns = [

    # comment/post/25/push
    url(r'^post/(?P<post_pk>[0-9]+)/push$', views.PostPostComment, name='post_comment'),

    # comment/post/25/
    url(r'^post/(?P<post_pk>[0-9]+)$', views.GetPostComment.as_view(), name='get_comments'),

]

