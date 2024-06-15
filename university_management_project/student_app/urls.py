from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('students/register/', views.register_student, name='register_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
]
