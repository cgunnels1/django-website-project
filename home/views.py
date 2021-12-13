from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return render(request, 'index.html')

def profile_view(request):
    return render(request, 'profile.html')

def login_view(request):
    return render(request, 'login.html')

