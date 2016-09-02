"""playlists Models."""
from django.db import models


class Playlist(models.Model):
    """Model that represents a playlist.

    Contains a name and is linked to SongEntries.
    The song's order in the playlist is represented by its order field.
    """
    name = models.TextField()

    def __str__(self):
        """Return the name of the playlist.

        >>> str(Playlist(name='Funk'))
        'Funk'
        """
        return self.name

    def __repr__(self):
        """Return the repr of this playlist.

        >>> repr(Playlist(name='Funk'))
        "Playlist(name='Funk')"
        """
        return 'Playlist(name={!r})'.format(self.name)


class SongEntry(models.Model):
    """Model representing a song in a playlist.

    Contains a title and artist.
    The playlist it is a part of and what order it is in the playlist is linked.
    """
    playlist = models.ForeignKey(Playlist)
    title = models.TextField()
    artist = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        """Return the artist and title of this song.

        >>> str(SongEntry(title='Title', artist='David', order=1))
        'David - Title'
        """
        return '{} - {}'.format(self.artist, self.title)

    def __repr__(self):
        """Return the repr of this song.

        >>> repr(SongEntry(title='Title', artist='David', order=1))
        "SongEntry(title='Title', artist='David', order=1)"
        """
        return 'SongEntry(title={!r}, artist={!r}, order={!r})'.format(
            self.title,
            self.artist,
            self.order,
        )
