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
    def clean(self):
        cleaned_data = super().clean()
        if self.instance.is_mentee:
            raise forms.ValidationError("A user cannot be both a mentor and a mentee.")
        return cleaned_data

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
    def clean(self):
        cleaned_data = super().clean()
        if self.instance.is_mentor:
            raise forms.ValidationError("A user cannot be both a mentor and a mentee.")
        return cleaned_data
    
# forms.py
class UserEditForm(forms.ModelForm):
    is_mentor = forms.BooleanField(label="Mentor", required=False)
    is_mentee = forms.BooleanField(label="Mentee", required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'emplid', 'major', 'preferred_language', 'is_mentor', 'is_mentee']
        mentor_field = forms.CharField(max_length=255, required=False)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class SignupForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
