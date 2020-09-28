from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .loginForm import LoginForm
from .registerForm import RegisterForm

# Create your views here.

def login_request(request):
    form = LoginForm
    return render(request,"main/login.html",context={"form":form})

def register(request):
    form = RegisterForm
    return render(request,"main/register.html",context={"form":form})