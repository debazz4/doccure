from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (ListView, TemplateView, DetailView, UpdateView, FormView)
from .models import DoctorProfile, DoctorEducation
from .forms import DoctorProfileForm, DoctorEducationForm, WorkExperience, Award, DoctorLocation

class HomeView(ListView):
    model = DoctorProfile
    template_name = "index.html"
    context_object_name = "doctors"

class DoctorProfileView(DetailView):
    model = DoctorProfile 
    template_name = "doctor-profile.html"
    context_object_name = "doctor"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()

        # Convert text field to list
        context['specialization_list'] = object.specialization.split(", ") #Split specialization text

        # For education list
        context["education_list"] = DoctorEducation.objects.filter(doctor=self.object)

        # For Awards
        context["awards_list"] = Award.objects.filter(doctor=self.object)

        # For Work Experience
        context["work_experience_list"] = WorkExperience.objects.filter(doctor=self.object)

        # For DoctorLocation
        context["doctor_location"] = DoctorLocation.objects.filter(doctor=self.object)
        
        return context

class DoctorDashboardView(TemplateView):
    #model = DoctorProfile
    template_name = "doctor-dashboard.html"
    #context_object_name = "doctor-dashboard"



# View to update Doctor Profile
class DoctorProfileUpdateView(UpdateView):
    model = DoctorProfile
    form_class = DoctorProfileForm
    template_name = "doctor_profile_update.html"

    def get_object(self, queryset=None):
        return get_object_or_404(DoctorProfile, user=request.user)

    def get_success_url(self):
        return reverse_lazy("doctor_profile_update") # Refresh the page

class DoctorEducationCreateView(FormView):
    template_name = "doctor_profile_update.html"
    form_class = DoctorEducationForm

    def form_valid(self, form):
        doctor = get_object_or_404(DoctorProfile, user=request.user)
        education = form.save(commit=False)
        education.doctor = doctor
        education.save()
        return redirect("doctor_profile_update")