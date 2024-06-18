from django import forms
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import *

# students forms
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__' 


#Registration and login forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    login = forms.CharField(label="Email, Phone Number, or Username")

    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data.get('login')
        password = cleaned_data.get('password')

        if login and password:
            user = authenticate(username=login, password=password)
            if not user:
                user = User.objects.filter(email=login).first()
                if user and user.check_password(password):
                    self.user_cache = user
                else:
                    user = User.objects.filter(phone_number=login).first()
                    if user and user.check_password(password):
                        self.user_cache = user
                    else:
                        raise forms.ValidationError("Invalid login credentials")
        return cleaned_data


#Department forms
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']

#Program forms
class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = "__all__"

## Faculty views 

class FacultyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__' 