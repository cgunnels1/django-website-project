from django.shortcuts import render
from django.http import HttpResponse
from .models import Song

# Create your views here.


def song_list_view(request):
    song_objects = Song.objects.all()
    context = {
        'song_objects': song_objects
    }
    if request.method == 'GET':
        
        print("Success")
        # form = SongForm(request.POST)
        # if form.is_valid():
        #     #return HttpResponse("Success")
        #     print("Success")
        # 
        # else:
        #     form = SongForm()

    return render(request, "playlist/index.html", context)

def song_play_view(request, id):
    song_objects = Song.objects.filter(id=id)
    context = {
        'song_objects': song_objects
    }
    return render(request, "playlist/song.html", context)