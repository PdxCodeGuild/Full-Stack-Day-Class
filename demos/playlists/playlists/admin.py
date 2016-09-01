"""playlists Admin Configuration."""
from django.contrib import admin

from . import models


admin.site.register(models.SongEntry)
admin.site.register(models.Playlist)
