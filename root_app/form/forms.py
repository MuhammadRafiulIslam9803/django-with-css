from django import forms

class StudentRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput )
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    # eta password and confirm password match kina check korbe
    # match korle form submit hobe
    # then validation error raise korbe match na hoile
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

class StudentDetailsForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    department = forms.CharField(max_length=100)
    semester = forms.IntegerField()
    phone = forms.IntegerField()
    
    def clean(self):
        cleaned_data = super().clean()
        id = cleaned_data.get("id")
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        department = cleaned_data.get("department")
        semester = cleaned_data.get("semester")
        phone = cleaned_data.get("phone")

        if not id or not name or not email or not department or not semester or not phone:
            raise forms.ValidationError("All fields are required.")