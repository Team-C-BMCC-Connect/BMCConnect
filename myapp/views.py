from django.http import JsonResponse
from myapp.forms import MentorForm, MenteeForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from .models import Mentee

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
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            # Process the form data for mentors
            # ...
            return JsonResponse({'success': True})
        else:
            # Return the form errors in JSON format
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
            form = MentorForm()
    return render(request, 'mentor_registration.html', {'form': form})

def mentee_registration(request):
    if request.method == 'POST':
        form = MenteeForm(request.POST)
        if form.is_valid():
            mentee = Mentee(
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                emplid=form.cleaned_data['emplid'],
                major=form.cleaned_data['major'],
                preferred_language=form.cleaned_data['preferred_language']
            )
            mentee.save()
            # ...
            return render(request, 'profile.html')
        else:
            # Return the form errors in JSON format
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = MenteeForm()
    
    return render(request, 'mentee_registration.html', {'form': form})

def mentor_registration(request):
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.save()  
            return JsonResponse({'success': True})
        else:
            # Return the form errors in JSON format
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = MentorForm()
    
    return render(request, 'mentor_registration.html', {'form': form})

def index(request):
    return render(request, 'home.html')

def mentors_view(request):
    return render(request, 'mentors.html')