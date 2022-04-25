from django.urls import path

from . import views

urlpatterns = [
    path('playlist/', views.song_list_view),
    path('playlist/<int:id>/', views.song_play_view),
]