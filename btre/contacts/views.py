from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from listings.models import Listing
from django.contrib.auth.models import User


def index(request):
    if request.method == 'POST':
        listing = Listing(pk=int(request.POST['listing_id']))
        listing_title = request.POST['listing_title']
        user = User(pk=int(request.POST['user_id']))
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if check_inquiry(listing, user):
            messages.info(request, 'Your already submitted this inquiry')
            return redirect('dashboard')

        contact = Contact(
            listing_title=listing_title,
            listing=listing,
            user=user,
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        contact.save()

        messages.success(request, 'Your request has been submitted, realtor will get back to you soon')

        return redirect('dashboard')

    return render(request, 'listings/listings.html')


def check_inquiry(listing, user):
    return Contact.objects.filter(listing=listing, user=user).exists()
