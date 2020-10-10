from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CourseList,CourseDetail

app_name = 'content'

urlpatterns = [
    path('', CourseList.as_view()),
    path('<int:pk>/', CourseDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)