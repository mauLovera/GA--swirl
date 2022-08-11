from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('playlist/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
  path('playlist/create/', views.PlaylistCreate.as_view(), name='playlist_create'),
]