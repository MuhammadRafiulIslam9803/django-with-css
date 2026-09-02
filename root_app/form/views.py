from django.shortcuts import render
from . forms import StudentDetailsForm, StudentRegistrationForm
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

def studentDetails (request):
    if request.method == 'POST':
        student_details_form = StudentDetailsForm(request.POST)
        if student_details_form.is_valid():
            
            id = student_details_form.cleaned_data['id']
            name = student_details_form.cleaned_data['name']
            email = student_details_form.cleaned_data['email']
            department = student_details_form.cleaned_data['department']
            semester = student_details_form.cleaned_data['semester']
            phone = student_details_form.cleaned_data['phone']
            
            # Save the form data to the model for table creation
            print("Student Details:", id, name, email, department, semester, phone)
    else:
        student_details_form = StudentDetailsForm(label_suffix=' =', initial={'id': 1, 'name': 'John Doe', 'email': 'default@email.com'})
            
    return render(request, 'form/studentDetails.html', {'student_details_form': student_details_form})