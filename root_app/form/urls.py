from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('sd/', views.studentDetails, name='studentDetails'),
]