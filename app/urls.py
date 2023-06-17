from django.urls import path
from .views import HomeViews, ScholarViews, CourseViews, PublicationViews

app_name = "Alhouda"

urls = urlpatterns = [
    path('', HomeViews.as_view(), name ='Home'),
    path('app/scholars/', ScholarViews.as_view(), name='scholar_list'),
    path('app/publications/', PublicationViews, name='publications'),
    path('app/courses/', CourseViews, name='courses')
]
