from django.shortcuts import render, redirect
from .models import Club
from .forms import ClubForm

def clubs_list_view(request):
    clubs = Club.objects.all()
    return render(request, 'clubs_2.html', {'clubs': clubs})
    
def create_club_view(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clubs')
    else:
        form = ClubForm()
    return render(request, 'create_club.html', {'form': form})

def edit_club(request, club_id):
    club = Club.objects.get(pk=club_id)
    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('/clubs')
    else:
        form = ClubForm(instance=club)
    return render(request, 'edit_club.html', {'form': form, 'club': club})
