from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery

# Create your views here.
def gallery_list_view(request):
    gallery_objects = Gallery.objects.all()
    context = {
        'gallery_objects': gallery_objects
    }
    return render(request, "gallery/index.html", context)