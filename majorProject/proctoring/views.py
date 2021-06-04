from django.shortcuts import render,redirect
from django.http import HttpResponse, request
import cv2
import numpy as np
from django.http import StreamingHttpResponse
from .camera import VideoCamera

# Create your views here.

def cheating(request):
    return render(request, 'cheating.html')

def homepage_new(request,cheating=False):
    if cheating:
        return redirect('proc/cheating')
    return render(
        request,
        "quiz_new.html",
    )

def homepage(request):
	return render(
					request,
					"quiz_new.html",
					)

def gen(request,camera):
    while True:
        len,frame = camera.get_frame()
        if(len!=1):
            print("cheating")
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(request,VideoCamera()),content_type = 'multipart/x-mixed-replace;boundary=frame')