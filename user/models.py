from django.db import models
from django.contrib.auth.models import User

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

AREA_CHOICES = [
    ('Dhaka', 'Dhaka'),
    ('Chittagong', 'Chittagong'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Barisal', 'Barisal'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Mymensingh', 'Mymensingh'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    area = models.CharField(max_length=100, choices=AREA_CHOICES)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
