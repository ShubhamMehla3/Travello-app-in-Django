from django.shortcuts import render
from .models import destinations
# Create your views here.

def index (request):

    dest1 = destinations()
    dest2 = destinations()
    dest3 = destinations()

    dest1.name = 'Mumbai'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'
    dest1.desc = 'The City that Never Sleeps'
    dest1.offer = False

    dest2.name = 'Kurukshetra'
    dest2.desc = 'The City of Everything'
    dest2.img = 'destination_2.jpg'
    dest2.price = 720
    dest2.offer = True

    dest3.name = 'Bengaluru'
    dest3.desc = 'The Beautiful City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests' : dests})