from django.db import models

# Create your models here.

class course(models.Model):
    course_name = models.CharField(max_length=300)
    course_id = models.IntegerField()
    course_info = models.TextField()
    cover_image_url = models.SlugField()
    videos_location = models.SlugField()
    instructor_name = models.CharField(max_length=300)
    course_slug = models.SlugField(default='course')
    course_thumbnail = models.ImageField(blank=True)
    def __str__(self):
        return self.course_name

class course_reviews(models.Model):
    course_id = models.ForeignKey(course,default=1,on_delete=models.SET_DEFAULT)
    reviewer_name = models.CharField(max_length=300)
    review_para = models.TextField()
    review_rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])

class tutorials(models.Model):
    tutorial_name = models.CharField(max_length=300)
    tutorial_description = models.TextField()
    tutorial_slug = models.SlugField(default='tut') 
    course_name = models.ForeignKey(course,default=1,on_delete=models.SET_DEFAULT)
    tutorial_video = models.FileField()

class instructor(models.Model):
    instructor_name = models.CharField(max_length=300)
    instructor_tagline = models.TextField()
    instructor_img = models.ImageField(blank=True)