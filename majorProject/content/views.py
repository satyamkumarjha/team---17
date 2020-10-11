from django.shortcuts import render

def contentView(request):
    return render(request,'content/courses.html')

def reviewsView(request):
    return render(request,'content/reviews.html')