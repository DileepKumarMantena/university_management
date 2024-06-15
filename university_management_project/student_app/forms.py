from django import forms
from .models import *

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__' 