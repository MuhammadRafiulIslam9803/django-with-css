from django.db import models
from django.db import models
# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=50)
    student_department = models.CharField(max_length=50)
    student_semester = models.IntegerField()
    student_phone = models.IntegerField()
    