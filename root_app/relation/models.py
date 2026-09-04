from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_reg = models.IntegerField()
    
        
class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

class course(models.Model):
    user = models.ManyToManyField(User)
    course_name = models.CharField(max_length=100)
    course_code = models.IntegerField()

    def course_students(self):
        return ", ".join(str(user) for user in self.user.all())