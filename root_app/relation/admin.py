from django.contrib import admin
from .models import Student, Teacher, course

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user' ,'student_name', 'student_reg')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user' ,'teacher_name', 'subject')

@admin.register(course)
class courseAdmin(admin.ModelAdmin):
    list_display = ('course_students' ,'course_name', 'course_code')
