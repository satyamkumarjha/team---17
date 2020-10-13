from django.shortcuts import render
import os
from django.conf import settings


def contentView(request):
    return render(request,'courses.html')

def reviewsView(request):
    return render(request,'reviews.html')

def kunalView(request):
    kunalFolder = os.path.join(settings.MEDIA_ROOT,'kunal')
    kunalFiles = os.listdir(kunalFolder)
    kunalCount = len(kunalFiles)
    for i in range(len(kunalFiles)):
        kunalFiles[i] = os.path.join(kunalFolder,kunalFiles[i])
    print(kunalCount)
    print(kunalFiles)
    return render(request,'kunal.html',{'files':kunalFiles})

def negiView(request):
    negiFiles = os.listdir(os.path.join(settings.MEDIA_ROOT,'negi'))
    negiCount = len(negiFiles)
    return render(request,'negi.html')

def prabhView(request):
    prabhFiles = os.listdir(os.path.join(settings.MEDIA_ROOT,'prabh'))
    prabhCount = len(prabhFiles)
    return render(request,'prabh.html')

def harwinderView(request):
    harwinderFiles = os.listdir(os.path.join(settings.MEDIA_ROOT,'harwinder'))
    harwinderCount = len(harwinderFiles)
    
    return render(request,'kunal.html')