from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from album.forms import AddForm
from .models import Album
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AddForm
    template_name = 'album/create.html'
    success_url = '/album'

class Delete(DeleteView):
    template_name = 'album/delete.html'

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Album, id=id)

    def get_success_url(self):
            return reverse('album:index')

class Update(UpdateView):
    
    template_name = 'album/update.html'
    form_class = AddForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Album, id=id)
    
    def get_success_url(self):
        return reverse('album:index')




def index(request):
    album_data = Album.objects.all()
    context = {
        'album_data': album_data

     }

    return render(request, 'album/index.html',context)