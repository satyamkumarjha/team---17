from django.shortcuts import render,HttpResponse,Http404
import os
from django.conf import settings
from .models import course,course_reviews,tutorials,instructor


def contentView(request):
    return render(
    request = request,
    template_name='courses.html' ,
    context= {"courses":course.objects.all()})

def single_slug(request,single_slug):
    courses = [i.course_slug for i in course.objects.all()]
    print(courses)

    if single_slug in courses:
        current_tutorials = []
        for c in course.objects.all():
            if c.course_slug == single_slug:
                current_course = c.course_name
                instr = c.instructor_name
        current_tutorials = []
        for t in tutorials.objects.all():
            print(current_course,t.course_name)
            if str(t.course_name) == str(current_course):
                print('true')
                current_tutorials.append(t)
        for i in instructor.objects.all():
            if i.instructor_name == instr:
                instructor_details = i
        print('current course:',current_course)
        print(current_tutorials)
        return render(request,'tutorials.html',context={'tuts':current_tutorials,'ins':instructor_details})

def test(request):
    return render(request,'videodisp.html',context={'tuts':tutorials.objects.all()})