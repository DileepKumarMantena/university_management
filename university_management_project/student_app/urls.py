# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('student_list/', views.student_list, name='student_list'),
    path('students/register/', views.register_student, name='register_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('logout/', views.logout_view, name='logout'),
    path('logout_success/', views.logout_success, name='logout_success')
]
