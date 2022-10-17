from ctypes.wintypes import MSG
from distutils.log import error
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect




  
def signup(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            return redirect('/')
        else:
            msg = 'Please fill in the blanks properly!'
            return render(request, 'signup.html', {'form': form , 'msg': msg})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})



def home(request): 
        return render(request, 'home.html')
   
  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard') #profile
        else:
            msg = 'Invalid Details'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
  
def profile(request): 
    return render(request, 'profile.html')
   
def signout(request):
    logout(request)
    return redirect('/signin')

def aboutus(request): 
    return render(request, 'aboutus.html')

def dashboard(request): 
    return render(request, 'dashboard.html')