from django.contrib import admin
from .models import CustomUser
from .models import Mentee

admin.site.register(CustomUser)
admin.site.register(Mentee)
