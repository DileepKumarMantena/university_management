# Generated by Django 5.0.4 on 2024-06-15 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0005_alter_student_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='profile_picture',
        ),
    ]
