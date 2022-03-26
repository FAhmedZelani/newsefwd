from datetime import datetime
from tkinter import Widget
from django import forms
from .models import Appointment, Contact


class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ('name', 'email', 'dept', 'datetime')
        


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'dept', 'message')
