from django.shortcuts import render

from . models import Student , Result

# Create your views here.
def collage(request):
    studentDetails = Student.objects.all()
    result = Result.objects.all()
    return render(request, 'collage/student.html',
                  {'studentDetails': studentDetails,
                   'result': result})
