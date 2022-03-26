from django.contrib import admin
from .models import Expert, Project, Testimonial, Service, Partner, Award, Appointment, Contact, Blog

# Register your models here.

class ExpertAdmin(admin.ModelAdmin):
    list_display = ['title', 'designation', 'image']
    search_fields = ['title']

admin.site.register(Expert, ExpertAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    

admin.site.register(Project, ProjectAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    

admin.site.register(Testimonial, TestimonialAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    

admin.site.register(Service, ServiceAdmin)

class PartnerAdmin(admin.ModelAdmin):
    list_display = [ 'image']
    

admin.site.register(Partner, PartnerAdmin)

class AwardAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    

admin.site.register(Award, AwardAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'dept', 'datetime']
    

admin.site.register(Appointment, AppointmentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'dept', 'services', 'message']
    

admin.site.register(Contact, ContactAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'image']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)






