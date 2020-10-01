from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .loginForm import LoginForm
from .registerForm import RegisterForm
from django.contrib import messages
# Create your views here.



def login_request(request):
    if request.method == "POST":
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now logged in as {username}")
                return redirect('main:homepage')
            else:
                messages.error(request,"Invalid Username or Password")
        else:
            messages.error(request,"Invalid Username or Password")
    form = LoginForm
    return render(request,"main/login.html",context={"form":form})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"New Account Created: {username}")
            login(request,user)
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}: form.error_messages[msg]")
    form = RegisterForm
    return render(request,"main/register.html",context={"form":form})

def googleLogin(request):
    return render(request, "main/googleLogin.html")