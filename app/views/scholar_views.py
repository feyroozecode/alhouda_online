from django.shortcuts import render, get_object_or_404 
from ..models import Scholar

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