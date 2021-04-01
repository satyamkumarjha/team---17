from django.shortcuts import render

# Create your views here.

def homepage(request):
    print(request.user)
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')