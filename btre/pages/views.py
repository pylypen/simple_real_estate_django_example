from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    return render(request, 'pages/index.html', {
        'listings': listings,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
    })


def about(request):
    realtors = Realtor.objects.order_by('-hire_date').all()[:3]
    mvp_realtor = Realtor.objects.filter(is_mvp=True).first()

    return render(request, 'pages/about.html', {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    })
