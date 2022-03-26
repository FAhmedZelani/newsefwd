from django.urls import path
from . import views

app_name = 'xit'

urlpatterns = [
    path('', views.index, name='index'),
    path('it-solutions/', views.itsolutions, name='it-solutions'),
    path('contact_form/', views.contact, name='contact_form'),
    path('search/', views.search, name='search'),
    
    path('about-us/', views.about, name='about-us'),
    path('contact-us/', views.contactus, name='contact-us'),
    path('blog/', views.blog_index, name='blog_index'),
    path('blog/<slug>/', views.blog_details, name='blog_details'),
   
]