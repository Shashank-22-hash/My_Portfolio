from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio, Certification

# Create your views here.
def index(request):
    
    home = Home.objects.latest('updated')
    
    about = About.objects.latest('updated')
    profile  = Profile.objects.filter(about= about)
    
    categories = Category.objects.all()
    
    portfolios = Portfolio.objects.all()
    
    certification = Certification.objects.all()
    
    
    context = {
        'home': home,
        'about': about,
        'profile': profile,
        'categories': categories,
        'portfolios': portfolios,
        'certification': certification,
        
        
    }
        
    return render(request, 'index.html', context)