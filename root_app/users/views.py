from django.shortcuts import render
from . forms import UserForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/home.html')
    else:
        form = UserForm()
        
    return render(request, 'users/register.html' , {'form': form})

def loginFrom(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Perform login logic here
            uname = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(uname, password)
            
            user = authenticate(request, username=uname, password=password)
            if user is not None:
                # User is authenticated, perform login
                login(request, user)
                return render(request, 'users/home.html')
    else:
        form = AuthenticationForm()
        
    return render(request, 'users/login.html', {'form': form})

def logoutForm(request):
    # Perform logout logic here
    logout(request)
    return render(request, 'users/login.html')
def password_reset(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return render(request, 'users/home.html')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, 'users/passwordReset.html', {'form': form})
    
    return render(request, 'users/login.html')