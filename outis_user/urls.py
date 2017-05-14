from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^logout$', login_required(views.LogoutView.as_view()), name='logout'),
    url(r'^profile$', login_required(views.ProfileView.as_view()), name='profile'),
    url(r'^peek/(?P<user_pk>[0-9a-f-]+)$', views.PeekUserView.as_view(), name='peek'),
    url(r'^destroy$', views.DestroyUser.as_view(), name='destroy'),
    #url(r'^validate$', views.validate, name='validate'),

    # /user/username/
    # url(r'^(?P<username>)[a-z]+$', views.fromUsernameToUid, name='fromUsernameToUid'),
]
