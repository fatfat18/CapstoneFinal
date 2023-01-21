from ctypes.wintypes import MSG
from distutils.log import error
from xml.dom import ValidationErr
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout , get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect , render
from django.contrib.auth import forms  
from django.contrib import messages  
from .forms import CustomUserCreationForm , updateform
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated
from .tokens import account_activation_token
from .models import editupdaterecord


from django.contrib.auth.models import User








def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
     

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('signin')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('/')










def activateEmail(request, user):
    mail_subject = "Activate your SafeSight Account."
    message = render_to_string("activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[user.email],)
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{user.email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {user.email}, check if you typed it correctly.')












@user_not_authenticated
def signup(request):
      if request.user.is_authenticated:
          return redirect('/dashboard')
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              user = form.save(commit=False)
              username = form.cleaned_data.get('username')
              email = form.cleaned_data.get('email')
              password = form.cleaned_data.get('password1')
              user = authenticate(username=username, password=password, email=email)
              user.is_active=False
              user.save()
              activateEmail(request,user)
              msg = 'Registered Successfully Please Verify Email to Login!'
              form = CustomUserCreationForm()
              return render(request, 'signup.html', {'form': form , 'msg': msg})
          else:
              msg = 'Please fill in the blanks properly!'
              return render(request, 'signup.html', {'form': form , 'msg': msg})
      else:
          form = CustomUserCreationForm()
          return render(request, 'signup.html', {'form': form})





def home(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        return render(request, 'home.html')


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password'].lower()
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('/dashboard') #profile
        else:
            msg = 'Invalid Details'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def editprofile(request,user):
    if request.user.is_authenticated:
        return render(request, 'editprofile.html')

        
        
def update(request):
    if request.method == 'POST':
        form = updateform(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            address = form.cleaned_data.get('address')
            user = authenticate(request, first_name=first_name, last_name=last_name,address=address)
            user.save()
            return redirect('/profile')




@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def editprofile(request):
    return render(request,'editprofile.html')

def displaydata(request):
    results=editupdaterecord.objects.all()
    return render(request,"profile.html",{"editupdaterecord":results})













def signout(request):
    logout(request)
    return redirect('/signin')

def aboutus(request):
    return render(request, 'aboutus.html')

@login_required
def dashboard(request):
    
    return render(request, 'dashboard.html')

@login_required
def reportcontents(request):
    return render(request, 'reportcontents.html')

def forgotpass(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    return render(request, 'forgotpass.html') 


     