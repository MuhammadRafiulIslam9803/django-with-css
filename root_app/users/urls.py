from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginFrom, name='login'),
    path('logout/', views.logoutForm, name='logout'),
    path('preset/', views.password_reset, name='passwordReset'),
]