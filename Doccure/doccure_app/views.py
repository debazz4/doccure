from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import DoctorProfile

class HomeView(ListView):
    model = DoctorProfile
    template_name = "index.html"
    context_object_name = "doctors"

class DoctorProfileView(DetailView):
    model = DoctorProfile 
    template_name = "doctor-profile.html"
    context_object_name = "doctor"


