from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Incorrect username or password')

    return render(request, 'accounts/login.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, 'Logout done')

    return redirect('login')


def register(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']

        # Validation
        if password != confirm_password:
            messages.error(request, 'Password do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username taken')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email taken')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            messages.success(request, 'User created successfully!')

            return redirect('login')

    return render(request, 'accounts/register.html')


def dashboard(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.order_by('-contact_date').filter(user=request.user.id).all()
        return render(request, 'accounts/dashboard.html', {
            "contacts": contacts
        })

    return redirect('login')
