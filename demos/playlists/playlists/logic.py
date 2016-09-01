"""playlists Logic."""
from . import models


def create_and_save_new_playlist(name):
    new_p = models.Playlist(name=name)
    new_p.save()


def get_next_order_for_playlist(playlist):
    songs_in_playlist = get_all_songs_for_playlist(playlist)
    orders = [song.order for song in songs_in_playlist]
    return max(orders, default=0) + 1


def create_song_entry(artist, title, playlist):
    new_se = models.SongEntry(
        artist=artist,
        title=title,
        playlist=playlist,
        order=get_next_order_for_playlist(playlist),
    )
    new_se.save()


def get_all_playlists():
    return models.Playlist.objects.all()


def get_playlist_by_id(id):
    return models.Playlist.objects.get(id=id)


def get_all_songs_for_playlist(playlist):
    return models.SongEntry.objects.filter(playlist=playlist).order_by('order')
