from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_per_month_choices, location_choices, unit_type_choices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'price_per_month_choices': price_per_month_choices,
        'location_choices': location_choices,
        'unit_type_choices': unit_type_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP 
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    # This is called "dictionary"
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)