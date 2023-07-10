from django.shortcuts import render
from .forms import MentorMenteeForm
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        form = MentorMenteeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Registration successful!'})
    else:
        form = MentorMenteeForm()
    
    return render(request, 'registration.html', {'form': form})

