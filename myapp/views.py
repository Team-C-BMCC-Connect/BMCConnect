from django.http import JsonResponse
from myapp.forms import MentorForm, MenteeForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm

def signin_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('clubs_list')  # Replace 'clubs_list' with your clubs list URL name
    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})

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
            # Process the form data for mentees
            # ...
            return JsonResponse({'success': True})
        else:
            # Return the form errors in JSON format
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = MenteeForm()
    
    return render(request, 'mentee_registration.html', {'form': form})

def index(request):
    return render(request, 'index.html')