from django.shortcuts import render, get_object_or_404
from .models import Scholar, Course, Publication

class ScholarViews:
    def scholarList(request):
        scholars = Scholar.objects.all()
        
        return render(request, 'app/scholars/scholars_list.html', scholars)

    def scholarDetails(request):
        scholar = get_object_or_404(Scholar.objects.all(),)
        
        return render(request, 'app/scholar/scholar_details.html', {'scholar': scholar})

    def scholar_detail(request, scholar_id):
        scholar = get_object_or_404(Scholar, id=scholar_id)
        return render(request, 'app/scholar_detail.html', {'scholar': scholar})
    
class PublicationViews: 
    def publications(request):
        publications = Publication.objects.all().order_by('-date_of_pub')
        
        return render(request, 'app/publications.html', {'publications': publications} )
    
class HomeViews:
    def home(request):
        return render(request, 'app/publications/home.html')


# Courses
class CourseViews():
    def courses(request):
        courses = Course.objects.all()
        
        return render(request, 'app/courses', {'courses', courses})
