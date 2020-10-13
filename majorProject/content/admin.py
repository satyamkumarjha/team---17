from django.contrib import admin
from .models import course,course_reviews,tutorials

# Register your models here.
admin.site.register(course)
admin.site.register(course_reviews)
admin.site.register(tutorials)