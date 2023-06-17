from django.urls import path
from .views import courses, publications, scholarList

urls = urlpatterns = [
    path('', courses, name ='Home'),
    path('scholars/', scholarList, name='scholar_list'),
    path('publications/', publications, name='publications'),
    path('courses/', courses, name='courses')
]
