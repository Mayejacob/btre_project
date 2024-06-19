from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    Listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] # limit to 3
    context = {
        'listings': Listings,
        'price_choices': price_choices, 
        'bedroom_choices': bedroom_choices, 
        'state_choices': state_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    
    context ={
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }
    return render(request, 'pages/about.html', context)
