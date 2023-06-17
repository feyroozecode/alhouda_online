from django.urls import path
from . import views

app_name = "Alhouda"

urls = urlpatterns = [
    path('', views.home, name ='Home'),
    path('scholars/', views.scholarList, name='scholar_list'),
    path('publications/', views.publications)
]
