"""playlists Logic."""
from . import models


def create_new_playlist(name):
    """Create a new playlist with a given name and return it.

    It will be saved and ready for use.

    >>> create_new_playlist('Funk')
    Playlist(name='Funk')
    >>> models.Playlist.objects.get(name='Funk')
    Playlist(name='Funk')
    """
    new_p = models.Playlist(name=name)
    new_p.save()
    return new_p


def _get_next_order_for_playlist(playlist):
    """Look at a playlist and determine what the next index is in the ordering of songs.

    >>> pl = models.Playlist(name='Funk')
    >>> pl.save()
    >>> models.SongEntry(artist='Artist', title='One', playlist=pl, order=1).save()
    >>> models.SongEntry(artist='Artist', title='Two', playlist=pl, order=2).save()
    >>> _get_next_order_for_playlist(pl)
    3
    """
    songs_in_playlist = get_all_songs_for_playlist(playlist)
    orders = [song.order for song in songs_in_playlist]
    return max(orders, default=0) + 1


def create_song_entry(artist, title, playlist):
    """Create a new song entry attached to the end of a given playlist.

    The song will be saved and ready for use.

    >>> pl = models.Playlist(name='Funk')
    >>> pl.save()
    >>> se = create_song_entry('Artist', 'David', pl)
    >>> models.SongEntry.objects.get(id=se.id)
    SongEntry(title='David', artist='Artist', order=1)
    """
    new_se = models.SongEntry(
        artist=artist,
        title=title,
        playlist=playlist,
        order=_get_next_order_for_playlist(playlist),
    )
    new_se.save()
    return new_se


def get_all_playlists():
    """Return all playlists.

    >>> models.Playlist(name='Funk').save()
    >>> list(get_all_playlists())
    [Playlist(name='Funk')]
    """
    return models.Playlist.objects.all()


def get_playlist_by_id(playlist_id):
    """Return a playlist by ID.

    >>> pl = models.Playlist(name='Funk')
    >>> pl.save()
    >>> get_playlist_by_id(pl.id) == pl
    True
    """
    return models.Playlist.objects.get(id=playlist_id)


def get_all_songs_for_playlist(playlist):
    """Return all songs in a playlist in order.

    >>> pl = models.Playlist(name='Funk')
    >>> pl.save()
    >>> models.SongEntry(artist='Artist', title='Two', playlist=pl, order=2).save()
    >>> models.SongEntry(artist='Artist', title='One', playlist=pl, order=1).save()
    >>> list(get_all_songs_for_playlist(pl))
    [SongEntry(title='One', artist='Artist', order=1), SongEntry(title='Two', artist='Artist', order=2)]
    """
    return models.SongEntry.objects.filter(playlist=playlist).order_by('order')
