from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = "Department_Table"

class Program(models.Model):
    program_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(null=True, blank=True)
    duration_years = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')

    class Meta:
        db_table = "Program_Table"


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
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='students')
    year_of_study = models.PositiveIntegerField()
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "Student_Table"


class Faculty(models.Model):
    FACULTY_RANK_CHOICES = [
        ('Professor', 'Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Lecturer', 'Lecturer')
                            ]

    faculty_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    joining_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='faculty')
    rank = models.CharField(max_length=20, choices=FACULTY_RANK_CHOICES)

    class Meta:
        db_table = "Faculty_Table"
