from django.shortcuts import render, redirect
from .models import Club
from .forms import ClubForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import CustomUser

@login_required
def profile_view(request):
    user = request.user
    clubs = user.clubs.all()
    return render(request, 'profile.html', {'user': user, 'clubs': clubs})
@login_required
def delete_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    club.delete()
    return redirect('/clubs')  # Redirect to the clubs list page after deleting the club

def join_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    user = request.user
    user.clubs.add(club)
    print(club)
    print(user.clubs.all())
    return redirect('/clubs')

def clubs_list_view(request):
    clubs = Club.objects.all()
    user_clubs = request.user.clubs.all()
    categories = Club.objects.values_list('category', flat=True).distinct()
    return render(request, 'clubs_2.html', {'clubs': clubs, 'categories': categories, 'user_clubs': user_clubs})
    
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
