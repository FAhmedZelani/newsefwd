from django.shortcuts import render
from .models import Expert, Project, Testimonial, Service, Partner, Award, Blog
from .forms import AppointmentForm, ContactForm
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.

def index(request):

    experts = Expert.objects.all()
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    services = Service.objects.all()
    partners = Partner.objects.all()
    awards = Award.objects.all()

    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)

        if appointment_form.is_valid():
            appointment_form.save()

            return HttpResponseRedirect(request.path_info)
        else:
            appointment_form = AppointmentForm()

     
    context = {
        
        'experts' : experts,
        'projects' : projects,
        'testimonials' : testimonials,
        'services' : services,
        'partners' : partners,
        'awards' : awards
     }

    return render(request, 'xit/index.html',context)


def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()

            return HttpResponseRedirect('/')


        else:
            contact_form = ContactForm()

     
    context = {
        
        
     }

    return render(request, 'xit/index.html',context)

def itsolutions(request):
    context = {

    }

    return render(request, 'xit/it-solutions.html', context)


def about(request):
    context = {

    }

    return render(request, 'xit/about-us.html', context)

def contactus(request):
    context = {

    }

    return render(request, 'xit/contact-us.html', context)

def blog_index(request):
    blogs = Blog.objects.all()

    context = {
        'blogs' : blogs,
    }

    return render(request, 'xit/blog/index.html', context)

def blog_details(request, slug):
    blogs = Blog.objects.get(slug = slug)

    context = {
        'blogs' : blogs,
    }

    return render(request, 'xit/blog/details.html', context)


def search(request):
    queryset1 = Expert.objects.all()
    queryset2 = Project.objects.all()
    queryset3 = Service.objects.all()

    query = request.GET.get('q')

    if query:
        queryset1 = queryset1.filter(
            Q(title__icontains=query ) | Q(designation__icontains=query ) 
        ).distinct()

    queryset2 = queryset2.filter(
            Q(title__icontains=query ) | Q(short_description__icontains=query ) |
            Q(category__icontains=query )
        ).distinct()
    
    queryset3 = queryset3.filter(
            Q(title__icontains=query ) | Q(short_description__icontains=query ) 
           
        ).distinct()

    context = {
        'queryset1' : queryset1,
        'queryset2' : queryset2,
        'queryset3' : queryset3,

        'query' : query
    }
    return render(request, 'xit/search.html', context)
    