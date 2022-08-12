from ast import Delete
from django.shortcuts import render, redirect
from .models import Playlist, Song
from django.urls import reverse
from .forms import SongForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home(request):
    playlist = Playlist.objects.all()
    return render(request, 'home.html', {'playlist': playlist})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def add_song(request, playlist_id):
    form = SongForm(request.POST)
    if form.is_valid():
        new_song = form.save(commit=False)
        new_song.playlist_id = playlist_id
        new_song.save()
    return redirect('playlist_detail', playlist_id=playlist_id)


def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    song_form = SongForm()
    return render(request, 'playlist/detail.html', {'playlist': playlist, 'song_form': song_form})


class Login(LoginView):
    template_name = 'login.html'


class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ['title', 'description', 'image_url']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlaylistUpdate(LoginRequiredMixin, UpdateView):
    model = Playlist
    fields = '__all__'


class PlaylistDelete(LoginRequiredMixin, DeleteView):
    model = Playlist
    fields = '__all__'
    sucess_url = '/'
