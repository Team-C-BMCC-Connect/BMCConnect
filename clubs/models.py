from django.conf import settings
from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    meeting_type = models.CharField(max_length=100, default='On Campus')
    hybrid_link = models.URLField(blank=True)
    advisor_name = models.CharField(max_length=100)
    advisor_email = models.EmailField()
    club_room = models.CharField(max_length=100)
    active = models.CharField(max_length=100, default='Active')