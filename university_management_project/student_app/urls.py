# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('student_list/', views.student_list, name='student_list'),
    path('students/register/', views.register_student, name='register_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('logout/', views.logout_view, name='logout'),
    path('logout_success/', views.logout_success, name='logout_success'),
    
    #department urls
    path('register_department/', views.register_department, name='register_department'),
    path('list/', views.department_list, name='department_list'),

    #programs urls
    path('register_program/', views.register_program, name='register_program'),
    path('programs_list/', views.program_list, name='programs_list'),
    
    #faculty urls
    path('register_faculty/', views.register_faculty, name='register_faculty'),
    path('faculty_list/', views.faculty_list, name='faculty_list'),
    path('faculty/edit/<int:faculty_id>/', views.edit_faculty, name='edit_faculty'),
    path('faculty/delete/<int:faculty_id>/', views.delete_faculty, name='delete_faculty'),

    #admin urls
    path('', views.admin_register, name='admin_register'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),


]
