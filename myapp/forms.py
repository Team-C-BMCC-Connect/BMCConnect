from django import forms
from myapp.models import CustomUser

class MentorMenteeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['is_mentor', 'is_mentee', 'mentor_field', 'mentee_field']
        # Add any additional fields or customization as needed

