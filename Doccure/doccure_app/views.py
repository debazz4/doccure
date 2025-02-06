from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import DoctorProfile

class HomeView(ListView):
    model = DoctorProfile
    template_name = "index.html"
    context_object_name = "doctors"

class DoctorProfileView(TemplateView):
    model = DoctorProfile 
    template_name = "doctor-profile.html"
