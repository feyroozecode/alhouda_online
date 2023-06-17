from django.urls import path
from .views import courses, publications, scholarList

urls = urlpatterns = [
    path('', courses, name ='Home'),
    path('app/scholars/', scholarList, name='scholar_list'),
    path('app/publications/', publications, name='publications'),
    path('app/courses/', courses, name='courses')
]
