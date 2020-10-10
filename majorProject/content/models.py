from django.db import models

# Create your models here.

class course(models.Model):
    course_name = models.CharField(max_length=300)
    course_id = models.IntegerField()
    course_info = models.TextField()
    cover_image_url = models.SlugField()
    videos_location = models.SlugField()
    instructor_name = models.CharField(max_length=300)
    instructor_qualification = models.CharField(max_length=300) 
    reviewer_name = models.CharField(max_length=300)
    review_para = models.TextField()
    review_rating = models.IntegerField()

    def __str__(self):
        return self.course_name
