from django.db import models

# Create your models here.
class StudentFormInfo(models.Model):
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=50)
    student_password = models.CharField(max_length=50)
    student_confirm_password = models.CharField(max_length=50)