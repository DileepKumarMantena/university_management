from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import  login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

def home(request):
    print('home view is called')
    return render(request, 'home.html')


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to a list of students or a success page
    else:
        form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form})

@login_required
def student_list(request):
    username = request.user.username 
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students, 'username': username})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to student list or success page
    else:
        form = StudentRegistrationForm(instance=student)
    
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')  # Redirect to student list or success page
    
    return render(request, 'confirm_delete.html', {'student': student})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None  # Handle non-authenticated user case if needed
    logout(request)
    return render(request, 'logout_success.html', {'username': username})

def logout_success(request):
    return render(request, 'logout_success.html')