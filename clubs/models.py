from django.conf import settings
from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100, verbose_name='Club Name')
    email = models.EmailField(verbose_name='Club Email')
    meeting_type = models.CharField(max_length=100, default='On Campus', verbose_name='Hybrid ( On Campus & Virtual )')
    hybrid_link = models.URLField(blank=True, verbose_name='Hybrid Link ( If Applicable )')
    advisor_name = models.CharField(max_length=100, verbose_name='Advisor Name')
    advisor_email = models.EmailField(verbose_name='Advisor Email')
    club_room = models.CharField(max_length=100, verbose_name='Club Room')
    active = models.CharField(max_length=100, default='Active')

    def __str__(self):
        return self.name