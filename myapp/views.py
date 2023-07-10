from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from myapp.forms import MentorForm, MenteeForm

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