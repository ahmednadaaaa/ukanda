from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
from store.models import  Cart
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def send_message(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
    else:  # في حالة GET request
        name = ""
        email = ""
        message = ""

    send_mail(
        'New Contact Form Submission',
        f'Name: {name}\nEmail: {email}\nMessage: {message}',
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        )

    return render(request, 'contact/contact.html', {'myinfo': myinfo})


def CheckOut(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
    else:  # في حالة GET request
        name = ""
        email = ""
        phone_number = ""

    send_mail(
        'New Contact Form Submission',
        f'Name: {name}\nEmail: {email}\nphone: {phone_number}',
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        )
    cartitems = []

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()

    context = {"cart": cart, "items": cartitems}


    return render(request, "contact/chekout.html", context)







    #ahmadinejadjvkviyut@gmail.com
