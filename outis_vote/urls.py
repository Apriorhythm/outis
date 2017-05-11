from django.conf.urls import url
from . import views

app_name = 'vote'

urlpatterns = [
    # /vote/post/25
    url(r'^post/(?P<post_pk>[0-9]+)$', views.VotePost, name='vote-post'),

    # /vote/comment/25
    url(r'^comment/(?P<comment_pk>[0-9]+)$', views.VoteComment, name='vote-comment'),

]

