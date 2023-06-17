from django.urls import path
from .my_views.home_views import HomeViews
from .my_views.publication_views import PublicationViews
from .my_views.scholar_views import ScholarViews 
from .my_views.course_views import CourseViews

app_name = "Alhouda"

urls = urlpatterns = [
    path('', HomeViews.home, name ='Home'),
    path('app/scholars/', ScholarViews, name='scholar_list'),
    path('app/publications/', PublicationViews, name='publications'),
    path('app/courses/', CourseViews, name='courses')
]
