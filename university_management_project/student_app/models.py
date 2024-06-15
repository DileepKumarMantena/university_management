from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Non-Binary'),
    ]

    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    enrollment_date = models.DateField()
    program = models.CharField(max_length=100)
    year_of_study = models.PositiveIntegerField()
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "Student_Table"