from django.shortcuts import render
from . forms import StudentRegistrationForm

# Create your views here.
def form(request):
    student_form = StudentRegistrationForm( label_suffix=' =', initial={'name': 'John Doe', 'email': 'default@email.com'})
    return render(request, 'form/form.html', {'student_form': student_form})