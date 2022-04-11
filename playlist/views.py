from django.shortcuts import render
from django.http import HttpResponse
from .models import Song

from django.views.decorators.csrf import csrf_protect

# from pygame import mixer
# mixer.init()

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
