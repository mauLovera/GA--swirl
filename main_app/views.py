from django.shortcuts import render
from .models import Playlist, Song

# Create your views here.
def home(request):
  playlist = Playlist.objects.all()
  return render(request, 'home.html', { 'playlist' : playlist })

def playlist_detail(request, playlist_id):
  playlist = Playlist.objects.get(id=playlist_id)
  return render(request, 'playlist/detail.html', { 'playlist' : playlist})