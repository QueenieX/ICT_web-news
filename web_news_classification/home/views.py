from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Newsarticles, Categories

# user need to login before access to home page
@login_required
def home(request):
    newsarticles = {
        'newsarticles' : Newsarticles.objects.all(),
        'categories' : Categories.objects.all()
        }
    
    return render(request, 'home.html', newsarticles)