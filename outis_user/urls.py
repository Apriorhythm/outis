from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),
    url(r'^profile$', views.ProfileView.as_view(), name='profile'),
    #url(r'^validate$', views.validate, name='validate'),

    # /user/username/
    # url(r'^(?P<username>)[a-z]+$', views.fromUsernameToUid, name='fromUsernameToUid'),
]
