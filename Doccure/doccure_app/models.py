from django.db import models
from django_countries.fields import CountryField
from localflavor.us.us_states import US_STATES

STATUS_CHOICES = (
    (0, "Not Available"),
    (1, "Available")
)
DOCTOR_CHOICES = (
    ("Dr", "Dr"), # Doctor
    ("MD", "MD"), # Doctor of Medicine
    ("DO", "DO",) # Doctor of Osteopathic Medicine
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
    min_price = models.IntegerField(default=0)
    high_price = models.IntegerField(default=1000)
    profile_image = models.ImageField()
    price_per_hour = models.IntegerField()
    feature_image = models.ImageField()
    feature_image2 = models.ImageField()
    feature_image3 = models.ImageField()
    feature_image4 = models.ImageField()
    specialization = models.TextField(help_text="Enter your specialized duties")
    about_me = models.TextField(max_length=700)
    availability = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    set_availability = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"

class DoctorEducation(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="education")
    school_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor} ({self.school_name})"

class WorkExperience(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="experience")
    clinic = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    years = models.CharField(max_length=3)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor} ({self.clinic})"

class Award(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="awards")
    month = models.CharField(max_length=255)
    year = models.IntegerField()
    award_name = models.CharField(max_length=255)
    comment = models.TextField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor} ({self.award_name})"

class DoctorLocation(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="doctor_location")
    clinic_name = models.CharField(max_length=250)
    start_day1 = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    end_day1 = models.CharField(max_length=10, choices=DAYS_OF_WEEK, blank=True, null=True)
    start_time1 = models.TimeField()
    end_time1 = models.TimeField()
    start_time1_1 = models.TimeField(blank=True, null=True)
    end_time1_1 = models.TimeField(blank=True, null=True)
    start_day2 = models.CharField(max_length=10, choices=DAYS_OF_WEEK, blank=True, null=True)
    end_day2 = models.CharField(max_length=10, choices=DAYS_OF_WEEK, blank=True, null=True)
    start_time2 = models.TimeField(blank=True, null=True)
    end_time2 = models.TimeField(blank=True, null=True)
    service_charge = models.IntegerField()
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=40, choices=US_STATES)
    country = CountryField()
    feature_image = models.ImageField()
    feature_image1 = models.ImageField()
    feature_image2 = models.ImageField()
    feature_image3 = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor} ({self.clinic_name})"


class PatientProfile(models.Model):
    pass