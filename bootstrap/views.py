from django.shortcuts import render
from .models import Album

# Create your views here.
def index(request):
    album_data = Album.objects.all()
    context = {
        'album_data': album_data

     }

    return render(request, 'index.html',context)