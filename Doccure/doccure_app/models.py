from django.db import models
from django_countries.fields import CountryField
from localflavor.us.us_states import US_STATES

STATUS_CHOICES = (
    (0, "Not Available"),
    (1, "Available")
)
DOCTOR_CHOICES = (
    ("Doctor", "Dr"),
    ("Doctor of Medicine", "MD"),
    ("Doctor of Osteopathic Medicine", "DO")
)

DAYS_OF_WEEK = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday")
)
# Create your models here.
#Create a model class for doctors
class DoctorProfile(models.Model):
    title = models.CharField(max_length=30, choices=DOCTOR_CHOICES)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    doc_type = models.CharField(max_length=30)
    degrees = models.CharField(max_length=30)
    specification = models.CharField(max_length=200)
    state = models.CharField(max_length=40, choices=US_STATES)
    country = CountryField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    min_price = models.IntegerField(default=0, blank=True, null=True)
    high_price = models.IntegerField(default=1000, blank=True, null=True)
    profile_image = models.ImageField()
    price_per_hour = models.IntegerField()
    feature_image = models.ImageField()
    feature_image2 = models.ImageField()
    feature_image3 = models.ImageField()
    feature_image4 = models.ImageField()
    specialization = models.TextField(help_text="Enter your specialized duties")
    availability = models.CharField(max_length=10, choices=DAYS_OF_WEEK, blank=True, null=True)
    set_availability = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"

class PatientProfile(models.Model):
    pass