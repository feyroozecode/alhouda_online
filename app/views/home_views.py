from django.shortcuts import render 

class HomeViews:
    def home(request):
        return render(request, 'publications/home.html')
