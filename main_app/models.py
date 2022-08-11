from django.db import models

# Create your models here.


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200, default='')
    # owner

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    song_url = models.URLField(max_length=200, default='')
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
