from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import bedroom_choices, price_choices, state_choices


def index(request):
    listing_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listing_list, 3)

    page_number = request.GET.get('page')
    page_listings = paginator.get_page(page_number)

    return render(request, 'listings/listings.html', {
        'listings': page_listings
    })


def listing(request, listing_id):
    listing_obj = get_object_or_404(Listing, pk=listing_id)

    return render(request, 'listings/listing.html', {
        'listing': listing_obj
    })


def search(request):
    query_set_list = Listing.objects.order_by('-list_date').all()

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set_list = query_set_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set_list = query_set_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set_list = query_set_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_set_list = query_set_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set_list = query_set_list.filter(price__lte=price)

    return render(request, 'listings/search.html', {
        'listings': query_set_list,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
        'values': request.GET
    })
