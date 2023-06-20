from django.urls import path
from .views import courses, publications, scholarList, scholar_detail

urls = urlpatterns = [
    path('', courses, name ='Home'),
    path('scholars/', scholarList, name='scholar_list'),
    # path('scholar_details/<int:id>', scholar_detail,  name='scholar_details'),
    path('publications/', publications, name='publications'),
    path('courses/', courses, name='courses')
]
