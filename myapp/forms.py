from django import forms
from myapp.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'major', 'preferred_language']
        
class MentorForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['availability', 'email', 'first_name', 'last_name', 'emplid', 'rsvp_session', 'training_availability', 'mhfa_certification']

    availability = forms.ChoiceField(choices=[
        ('morning', 'In the morning (9:45 AM - 11:45 AM)'),
        ('afternoon', 'In the afternoon (3:00 PM - 5:00 PM)'),
        ('both', 'Both'),
        ('conflicts', 'Neither, I have scheduling conflicts, please follow up'),
    ])
    
    rsvp_session = forms.ChoiceField(choices=[
        ('07/06', '07/06 (Thursday) at 12:00 PM - 1:30 PM'),
        ('06/10', '06/10 (Monday) at 3:00 PM - 4:30 PM'),
        ('follow_up', 'I cannot attend either session, please follow up'),
    ])
    
    training_availability = forms.MultipleChoiceField(choices=[
        ('08/16', '08/16 Wednesday'),
        ('08/17', '08/17 Thursday'),
        ('08/18', '08/18 Friday'),
        ('08/19', '08/19 Saturday'),
        ('08/21', '08/21 Monday'),
        ('08/22', '08/22 Tuesday'),
        ('08/23', '08/23 Wednesday'),
        ('08/24', '08/24 Thursday'),
    ], widget=forms.CheckboxSelectMultiple)
    
    mhfa_certification = forms.ChoiceField(choices=[
        ('yes', 'Yes'),
        ('no', 'No'),
    ])


class MenteeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'emplid', 'major', 'preferred_language']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
