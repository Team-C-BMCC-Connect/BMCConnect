from django import forms
from myapp.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserMentor(forms.ModelForm):
    AVAILABILITY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]
    availability = forms.MultipleChoiceField(choices=AVAILABILITY_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = CustomUser
        fields = ['major', 'preferred_language', 'availability']
        mentor_field = forms.CharField(max_length=255, required=False)


class UserMentee(forms.ModelForm):
    AVAILABILITY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]
    availability = forms.MultipleChoiceField(choices=AVAILABILITY_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = CustomUser
        fields = ['major', 'preferred_language', 'availability']
        mentee_field = forms.CharField(max_length=255, required=False)

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'emplid', 'major', 'preferred_language']
        mentor_field = forms.CharField(max_length=255, required=False)
        


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
