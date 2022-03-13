from django.shortcuts import render
from .models import Carousel

# Create your views here.
def index(request):
    carousel_data = Carousel.objects.all()
    context = {
        'carousel_data': carousel_data

     }

    return render(request, 'carousel/index.html',context)