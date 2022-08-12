from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/login/', views.Login.as_view(), name='login'),
  path('accounts/signup/', views.signup, name='signup'),
  
  path('playlist/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
  path('playlist/create/', views.PlaylistCreate.as_view(), name='playlist_create'),
  path('playlist/<int:pk>/update/', views.PlaylistUpdate.as_view(), name='playlist_update'),  
  path('playlist/<int:pk>/delete/', views.PlaylistDelete.as_view(), name='playlist_delete'),
  path('playlist/<int:playlist_id>/add_song/', views.add_song, name='add_song')
]