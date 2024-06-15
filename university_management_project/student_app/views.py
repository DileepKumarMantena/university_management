from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from .models import *


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to a list of students or a success page
    else:
        form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

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