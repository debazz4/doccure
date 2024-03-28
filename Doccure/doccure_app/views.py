from django.shortcuts import render
from django.views.generic import ListView
from .models import DoctorProfile

class HomeView(ListView):
    model = DoctorProfile
    template_name = "index.html"