from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.index_view),
    path('', views.song_list_view),
]