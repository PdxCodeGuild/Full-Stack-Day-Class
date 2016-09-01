"""playlists URL Configuration

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

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_index, name='index'),
    url(r'^add$', views.render_add_playlist, name='add_playlist'),
    url(r'^add/submit$', views.render_add_playlist_ack, name='add_playlist_submit'),
    url(r'^playlist/(?P<playlist_id>.+)/$', views.render_playlist, name='playlist'),
    url(r'^playlist/(?P<playlist_id>.+)/add$', views.render_add_song, name='add_song'),
    url(r'^playlist/(?P<playlist_id>.+)/add/submit$', views.render_add_song_ack, name='add_song_submit'),

]
