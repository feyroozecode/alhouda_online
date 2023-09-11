from django.shortcuts import render, get_object_or_404
from .models import Scholar, Course, Publication

def scholar_list(request):
    scholars = Scholar.objects.all()
    return render(request, 'app/scholars/home.html', {'scholars':  scholars})

def scholar_detail(request, scholar_id):
    scholar = get_object_or_404(Scholar.objects.get(scholar_id), id=scholar_id)
    context = {'scholar': scholar}
    return render(request, 'app/scholars/details.html', context)

def publications(request):
    publications = Publication.objects.all().order_by('-date_of_pub')
    return render(request, 'app/publications.html', {'publications': publications} )
    
def home(request):
    return render(request, 'app/publications/home.html')

# Courses
def courses(request):
    courses = Course.objects.all()
    return render(request, 'app/courses/home.html', {'courses': courses})
