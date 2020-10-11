from rest_framework import serializers
from content.models import course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = ['course_name', 'course_id', 'course_info', 'cover_image_url', 'videos_location', 'instructor_name',
         'instructor_qualification']