from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import location_choices, price_per_month_choices, unit_type_choices

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(facility__icontains=keywords)

    # Sub-district
    if 'sub_district' in request.GET:
        sub_district = request.GET['sub_district']
        if sub_district:
            queryset_list = queryset_list.filter(sub_district__iexact=sub_district)

    # Location
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            queryset_list = queryset_list.filter(location__iexact=location)

    # Unit Type
    if 'unit_type' in request.GET:
        unit_type = request.GET['unit_type']
        if unit_type:
            queryset_list = queryset_list.filter(unit_type__iexact=unit_type)

    # Price
    if 'price_per_month' in request.GET:
        price_per_month = request.GET['price_per_month']
        if price_per_month:
            queryset_list = queryset_list.filter(price_per_month__lte=price_per_month)

    context = {
        'location_choices': location_choices,
        'unit_type_choices': unit_type_choices,
        'price_per_month_choices': price_per_month_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)