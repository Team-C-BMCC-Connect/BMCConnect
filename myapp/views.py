from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm, UserEditForm, UserMentor, UserMentee
from .models import Mentee, Mentor
from .matching import match_mentors_with_mentees



def signout_view(request):
    logout(request)
    return redirect('index')

def signin_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'home' with the name of your home page URL pattern
            else:
                return render(request, 'signin.html', {'error': 'Invalid credentials'})
        else:
            return render(request, 'signin.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Replace 'signin' with your sign-in URL name
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def mentor_registration(request):
    if not request.user.is_authenticated:
        return redirect('/signin')
    user = request.user
    mentor = Mentor.objects.filter(user=user).first()

    if request.method == 'POST':
        form = UserMentor(request.POST, instance=user)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.is_mentor = True
            mentor.save()
            return redirect('matchmaking')  # Replace 'matchmaking' with the appropriate URL name for the matchmaking view
    else:
        form = UserMentor(instance=user)

    return render(request, 'mentor_registration.html', {'form': form})

def mentee_registration(request):
    if not request.user.is_authenticated:
        return redirect('/signin')
    user = request.user
    mentee = Mentee.objects.filter(user=user).first()

    if request.method == 'POST':
        form = UserMentee(request.POST, instance=user)
        if form.is_valid():
            mentee = form.save(commit=False)
            mentee.is_mentee = True
            mentee.save()
            return redirect('matchmaking')  # Replace 'matchmaking' with the appropriate URL name for the matchmaking view
    else:
        form = UserMentee(instance=user)

    return render(request, 'mentee_registration.html', {'form': form})

def edit_profile_view(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Replace 'profile' with the name of your profile URL pattern
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

def index(request):
    return render(request, 'home.html')

def mentors_view(request):
    return render(request, 'mentors.html')

def demo_view(request):
    return render(request, 'demo.html')


def mentors_list_view(request):
    mentors = Mentor.objects.all()
    context = {'mentors': mentors}
    return render(request, 'mentors_list.html', context)

def mentees_list_view(request):
    mentees = Mentee.objects.all()
    context = {'mentees': mentees}
    return render(request, 'mentees_list.html', context)
def matchmaking_view(request):
    user = request.user
    mentors = Mentor.objects.all()
    mentees = Mentee.objects.all()

    context = {
        'user': user,
        'mentors': mentors,
        'mentees': mentees,
    }

    return render(request, 'matchmaking.html', context)



