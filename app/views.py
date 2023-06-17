from django.shortcuts import render, get_object_or_404
from .models import Scholar, Publication

# Views

def publications(request):
    publications = Publication.objects.all().order_by('-date_of_pub')
    
    return render(request, 'publications.html', {'publications': publications} )