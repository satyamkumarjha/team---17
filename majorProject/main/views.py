from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'main/home.html')

def contact(request):
    return render(request,'main/contact.html')