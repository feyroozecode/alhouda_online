from django.shortcuts import render 
from models import Course

class CourseViews:
    def courses(request):
        courses = Course.objects.all()
        
        return render(request, 'app/courses', {'courses', courses})