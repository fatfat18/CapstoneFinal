from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form 
from django.contrib.auth import get_user_model 




  
class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='Username', min_length=3, max_length=150)
    email = forms.EmailField(label='Email')  
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput) 


  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist!")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist!")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Passwords don't match!")  
        return password2  



    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1'],

        )
        return user  









from django.contrib.auth.models import User
from django.db import models




class UpdateNamesForm(forms.Form):

    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    address = forms.CharField(max_length=150)
    phonenumber = forms.IntegerField()



    def save(self,username):
        User = get_user_model()
        user = User.objects.get(username=username)
        user.address = self.cleaned_data['address']
        user.phonenumber = self.cleaned_data['phonenumber']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()













#from .models import user_details
#
#class UpdateUserDetailsForm(forms.ModelForm):
#    class Meta:
#        model = user_details
#        fields = ['first_name', 'last_name', 'address', 'phonenumber']
#
#
#        def save(self):
#            self.address = self.cleaned_data['address']
#            self.phonenumber = self.cleaned_data['phonenumber']
#            self.first_name = self.cleaned_data['first_name']
#            self.last_name = self.cleaned_data['last_name']
#            self.save()