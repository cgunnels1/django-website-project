from django.shortcuts import render
from django.http import HttpResponse
from .models import Song


# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index_view(request):
#     return render(request, 'playlist/index.html')

def song_list_view(request):
    song_objects = Song.objects.all()
    context = {
        'song_objects': song_objects
    }
    return render(request, "playlist/index.html", context)

# def Audio_store(request):
#     if request.method == 'POST':
#         form = AudioForm(request.POST,request.FILES or None)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('successfully uploaded')
#     else:
#         form = AudioForm()
#     return render(request, 'playlist/aud.html', {'form' : form})

