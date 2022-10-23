from django.http import HttpResponse, HttpRequest
from django.template import Template
from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    # dest1 = Destination()
    # dest1.name = 'Nairobi'
    # dest1.price = 200
    # dest1.desc = 'Place of cool waters'
    # dest1.pic = 'package-bg1.jpg'

    # dest2 = Destination()
    # dest2.name = 'Naivasha'
    # dest2.price = 100
    # dest2.desc = 'City that never sleeps'
    # dest2.pic = 'about-bg.png'

    # dest3 = Destination()
    # dest3.name = 'Mombasa'
    # dest3.price = 300
    # dest3.desc = 'Place of sandy Beaches'
    # dest3.pic = 'about-bg.png'

    # dest = [dest1, dest2, dest3]
    dest = Destination.objects.all()

    return render(request, 'index.html', {'dest':dest})

