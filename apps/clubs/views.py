from django.shortcuts import render
from .models import Club

def clubs_list_view(request):
    clubs = Club.objects.all()
    return render(request, 'clubs_2.html', {'clubs': clubs})
    
