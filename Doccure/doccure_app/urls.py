from django.urls import path
from .views import (HomeView, DoctorProfileView, DoctorDashboardView)

app_name = 'doccure_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('doctor-profile/<int:pk>/', DoctorProfileView.as_view(), name='doctor-profile'),
    path('doctor-dashboard/', DoctorDashboardView.as_view(), name='doctor-dashboard'),
]