from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_mentor = models.BooleanField(default=False)
    is_mentee = models.BooleanField(default=False)
    mentor_field = models.CharField(max_length=255, blank=True)
    availability = models.CharField(max_length=255, blank=True)
    emplid = models.CharField(max_length=255, blank=True)
    rsvp_session = models.CharField(max_length=255, blank=True)
    training_availability = models.CharField(max_length=255, blank=True)
    mhfa_certification = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    major = models.CharField(max_length=255, blank=True)
    preferred_language = models.CharField(max_length=255, blank=True)
    clubs = models.ManyToManyField('clubs.Club', related_name='members')

    def save(self, *args, **kwargs):
        if self.is_mentor:
            self.availability = ''
            self.emplid = ''
            self.rsvp_session = ''
            self.training_availability = ''
            self.mhfa_certification = ''
        if self.is_mentee:
            self.availability = ''
            self.emplid = ''
            self.rsvp_session = ''
            self.training_availability = ''
            self.mhfa_certification = ''
        super().save(*args, **kwargs)

class Mentee(models.Model):
    email = models.EmailField(verbose_name='Mentee Email')
    first_name = models.CharField(max_length=100, verbose_name='Mentee First Name')
    last_name = models.CharField(max_length=100, verbose_name='Mentee Last Name')
    emplid = models.IntegerField(default=0, verbose_name='EmplID')
    major = models.CharField(max_length=100, verbose_name='Mentee Major')
    preferred_language = models.CharField(max_length=100, verbose_name='Preferred Language')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Mentee"

class Mentor(models.Model):
    availability = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    emplid = models.CharField(max_length=255, blank=True)
    rsvp_session = models.CharField(max_length=255, blank=True)
    training_availability = models.CharField(max_length=255, blank=True)
    mhfa_certification = models.CharField(max_length=255, blank=True)

    # Additional fields to connect with CustomUser model
    user = models.OneToOneField('myapp.CustomUser', on_delete=models.CASCADE, related_name='mentor')

    # Your other fields can be added here if you have any specific fields for the Mentor model.

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Mentor"



    
