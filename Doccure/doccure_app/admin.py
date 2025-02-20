from django.contrib import admin
from .models import DoctorProfile, DoctorEducation, WorkExperience, Award
# Register your models here.

admin.site.register([DoctorProfile, DoctorEducation, WorkExperience, Award])