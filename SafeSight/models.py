from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout , get_user_model 
from django.contrib.auth.models import User
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form 
from django.contrib.auth import get_user_model 






#class user_details(AbstractBaseUser):
#    userId = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    first_name = models.CharField(max_length=150)
#    last_name = models.CharField(max_length=150)
#    phonenumber = models.IntegerField()
#    address = models.CharField(max_length=150)
#    USERNAME_FIELD = 'userId'
#    


    