"""playlists Views."""
from django.shortcuts import render

from . import logic


def render_index(request):
    playlists = logic.get_all_playlists()

    template_args = {
        'playlists': playlists,
    }
    return render(request, 'playlists/index.html', template_args)


def render_playlist(request, playlist_id):
    playlist = logic.get_playlist_by_id(playlist_id)
    songs = logic.get_all_songs_for_playlist(playlist)

    template_args = {
        'playlist': playlist,
        'songs': songs,
    }
    return render(request, 'playlists/playlist.html', template_args)


def render_add_playlist(request):
    return render(request, 'playlists/add_playlist.html', {})


def render_add_playlist_ack(request):
    new_playlist_name = request.POST['name']

    logic.create_new_playlist(new_playlist_name)

    template_args = {
        'playlist_name': new_playlist_name,
    }
    return render(request, 'playlists/add_playlist_ack.html', template_args)


def render_add_song(request, playlist_id):
    playlist = logic.get_playlist_by_id(playlist_id)

    template_args = {
        'playlist': playlist,
    }
    return render(request, 'playlists/add_song.html', template_args)


def render_add_song_ack(request, playlist_id):
    song_title = request.POST['title']
    song_artist = request.POST['artist']
    playlist = logic.get_playlist_by_id(playlist_id)

    logic.create_song_entry(song_title, song_artist, playlist)

    template_args = {
        'song_title': song_title,
        'song_artist': song_artist,
        'playlist_name': playlist.name,
    }
    return render(request, 'playlists/add_song_ack.html', template_args)
