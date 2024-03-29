from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber
# Create your views here.

def home(request):
    slider=Slider.objects.all()
    teams=Team.objects.all()
    featured_youtubers=Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_tubers=Youtuber.objects.order_by('-created_date')
    data = {
        'sliders':slider,
        'teams':teams,
        'featured_youtubers':featured_youtubers,
        'all_tubers':all_tubers,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request, 'webpages/about.html', data)

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')

