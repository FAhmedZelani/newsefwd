from datetime import datetime
from django.db import models
from django.urls import reverse

# Create your models here.

#Models for home page..
class Expert(models.Model):
    title = models.CharField(max_length=50)
    designation = models.CharField(max_length=20)
    image = models.ImageField(upload_to='experts/')
    social_fb = models.URLField(blank=True, null=True)
    social_github = models.URLField(blank=True, null=True)
      
    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='projects/')
     
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='testimonial/')
     
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    image = models.ImageField(upload_to='services/')
     
    def __str__(self):
        return self.title

class Partner(models.Model):
    image = models.ImageField(upload_to='partner/')
    image_hover = models.ImageField(upload_to='partner/', blank=True)

class Award(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    image = models.ImageField(upload_to='award/')
     
    def __str__(self):
        return self.title

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=False, auto_now = False, blank=True)
     
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    services = models.TextField()
    message = models.TextField()
     
    def __str__(self):
        return self.name



class Blog(models.Model):
    
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)
    short_description = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/')
    image_details = models.ImageField(upload_to='blog/', blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("xit:blog_details", kwargs={
            "slug": self.slug
            }) 

