from rest_framework import generics
from content.models import course

from content.api.serializers import CourseSerializer

class CourseList(generics.ListCreateAPIView):
    queryset = course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = course.objects.all()
    serializer_class = CourseSerializer