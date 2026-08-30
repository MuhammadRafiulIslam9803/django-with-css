from django.shortcuts import render

from . models import Student

# Create your views here.
def collage(request):
    studentDetails = Student.objects.all()
    return render(request, 'collage/student.html', {'studentDetails': studentDetails})