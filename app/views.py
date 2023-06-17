from django.shortcuts import render, get_object_or_404
from .models import Scholar, Course

# Views
def scholarList(request):
    scholars = Scholar.objects.all()
    
    return render(request, 'scholars/scholars_list.html', scholars)

def scholarDetails(request):
    scholar = get_object_or_404(Scholar.objects.all(),)
    
    return render(request, 'scholar/scholar_details.html', {'scholar': scholar})
