"""outis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from django.conf import settings

# My Urls
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^media/(?P<path>.*)/$', serve, {"document_root": settings.MEDIA_ROOT}),

    url(r'', include('outis_base.urls')),
    url(r'^user/', include('outis_user.urls')),
    url(r'^post/', include('outis_post.urls')),
    url(r'^collection/', include('outis_collection.urls')),
    url(r'^comment/', include('outis_comment.urls')),
    url(r'^vote/', include('outis_vote.urls')),

    url(r'^search/', include('haystack.urls')),


]




