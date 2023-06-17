from django.shortcuts import render
from ..models import Scholar, Publication

class PublicationViews: 
    def publications(request):
        publications = Publication.objects.all().order_by('-date_of_pub')
        
        return render(request, 'publications.html', {'publications': publications} )