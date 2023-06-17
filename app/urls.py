from django.urls import path
from .views import HomeViews, ScholarViews, PublicationViews, CourseViews

urls = urlpatterns = [
    path('', HomeViews.home, name ='Home'),
    path('app/scholars/', ScholarViews.scholarList, name='scholar_list'),
    path('app/publications/', PublicationViews.publications, name='publications'),
    path('app/courses/', CourseViews.courses, name='courses')
]
