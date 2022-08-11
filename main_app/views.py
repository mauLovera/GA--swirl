from django.shortcuts import render
from .models import Playlist, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
  playlist = Playlist.objects.all()
  return render(request, 'home.html', { 'playlist' : playlist })

def playlist_detail(request, playlist_id):
  playlist = Playlist.objects.get(id=playlist_id)
  return render(request, 'playlist/detail.html', { 'playlist' : playlist})

class PlaylistCreate(CreateView):
  model = Playlist
  fields = '__all__'