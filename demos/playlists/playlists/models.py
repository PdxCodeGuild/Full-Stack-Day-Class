from django.db import models


class Playlist(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Playlist(name={!r})'.format(self.name)


class SongEntry(models.Model):
    playlist = models.ForeignKey(Playlist)
    title = models.TextField()
    artist = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return '{} - {}'.format(self.artist, self.title)

    def __repr__(self):
        return 'SongEntry(title={!r}, artist={!r}, order={!r})'.format(
            self.title,
            self.artist,
            self.order,
        )
