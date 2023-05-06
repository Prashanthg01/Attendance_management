# attendance/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    # add other fields for student details as needed

    def __str__(self):
        return self.name

class Attendance(models.Model):
    CLASS_CHOICES = (
        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        # add more choices as needed
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    datee = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    class_name = models.CharField(max_length=255)
    session = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.student.name} - {self.date}'
