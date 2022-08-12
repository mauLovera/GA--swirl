from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('playlist_detail', kwargs={'playlist_id': self.id})

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    song_url = models.URLField(max_length=200, default='')
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
