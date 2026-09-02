from django.shortcuts import render
from . forms import StudentRegistrationForm
from . models import StudentFormInfo

# Create your views here.
def form(request):
    if request.method == 'POST':
        student_form = StudentRegistrationForm(request.POST)
        if student_form.is_valid():
            # Process the form data (e.g., save to database)
            name = student_form.cleaned_data['name']
            email = student_form.cleaned_data['email']
            password = student_form.cleaned_data['password']
            confirm_password = student_form.cleaned_data['confirm_password']
            
            # Save the form data to the model for table creation
            student_info = StudentFormInfo(student_name=name, student_email=email, student_password=password, student_confirm_password=confirm_password)
            student_info.save()
            
            # You can add your logic here to handle the form data
            
            return render(request, 'form/success.html', {'name': name})
    else:
       student_form = StudentRegistrationForm( label_suffix=' =', initial={'name': 'John Doe', 'email': 'default@email.com'})
       
    return render(request, 'form/form.html', {'student_form': student_form})