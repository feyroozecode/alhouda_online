from django.urls import path
from .views import courses, publications, scholar_list, scholar_detail

urls = urlpatterns = [
    path('', courses, name ='Home'),
    path('scholars/', scholar_list, name='scholar_list'),
    path('scholars/<int:scholar_id>/details', scholar_detail,  name='scholar_details'),
    path('publications/', publications, name='publications'),
    path('courses/', courses, name='courses')
]