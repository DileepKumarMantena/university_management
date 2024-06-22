from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import  login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

### Home and login views
def home(request):
    print('home view is called')
    return render(request, 'home.html')

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


#####Student views

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list') 
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


####Department Views


def register_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Redirect to the department list after saving
    else:
        form = DepartmentForm()
    return render(request, 'register_department.html', {'form': form})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})


###Program views

def register_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('programs_list')  # Redirect to the Programs  list after saving
    else:
        form = ProgramForm()
    return render(request, 'register_program.html', {'form': form})

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'programs_list.html', {'programs': programs})


### faculty views

def register_faculty(request):
    if request.method == 'POST':
        form = FacultyRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('faculty_list') 
    else:
        faculty = FacultyRegistrationForm()
    return render(request, 'register_faculty.html', {'faculty': faculty})

def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty_list.html', {'faculties': faculties})

def edit_faculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    if request.method == 'POST':
        form = FacultyRegistrationForm(request.POST, request.FILES, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')  # Redirect to student list or success page
    else:
        form = FacultyRegistrationForm(instance=faculty)
    
    return render(request, 'edit_faculty.html', {'form': form})

def delete_faculty(request, faculty_id):
    faculty = get_object_or_404(Student, id=faculty_id)
    if request.method == 'POST':
        faculty.delete()
        return redirect('faculty_list')  # Redirect to faculty list or success page
    
    return render(request, 'confirm_delete_faculty.html', {'faculty': faculty})

