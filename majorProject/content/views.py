from django.shortcuts import render

def contentView(request):
    return render(request,'courses.html')

def reviewsView(request):
    return render(request,'reviews.html')