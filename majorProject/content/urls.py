from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('', views.contentView),
    path('reviews/', views.reviewsView),
]

#urlpatterns = format_suffix_patterns(urlpatterns)