from django import forms
from .models import DoctorProfile, DoctorEducation, WorkExperience, Award

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['title', 'First_Name', 'Last_Name', 'doc_type',
        'degrees', 'specification', 'state', 'country', 'status', 
        'min_price', 'high_price', 'profile_image', 'price_per_hour', 
        'feature_image', 'feature_image2', 'feature_image3', 'feature_image4', 
        'specialization', 'about_me', 'availability', 'set_availability']

class DoctorEducationForm(forms.ModelForm):
    class Meta:
        model = DoctorEducation
        fields = ['school_name', 'degree', 'duration']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['clinic', 'duration']

class AwardsForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['month_and_year', 'award_name', 'comment']