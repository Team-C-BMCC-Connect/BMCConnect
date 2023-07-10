from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_mentor = models.BooleanField(default=False)
    is_mentee = models.BooleanField(default=False)
    # Add additional fields for mentor or mentee information
    # For example:
    mentor_field = models.CharField(max_length=255, blank=True)
    mentee_field = models.CharField(max_length=255, blank=True)
