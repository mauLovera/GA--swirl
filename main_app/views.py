from django.shortcuts import render
from .models import Playlist, Song

# Create your views here.
def home(request):
  playlist = Playlist.objects.all()
  return render(request, 'home.html', { 'playlist' : playlist })