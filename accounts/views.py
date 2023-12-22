from audioop import reverse
from urllib import request
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from .models import Profile
from .forms import UserForm, ProfileForm, SignupForm


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')  # تصحيح هذا السطر

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def profile(request, slug):
    profile = get_object_or_404(Profile, user__username=slug)
    return render(request, 'account/profile.html', {'profile': profile})


def profile_edit(request, slug):
    profile = get_object_or_404(Profile, user__username=slug)

    if request.method == 'POST':
        userform = UserForm(request.POST, instance=profile.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()

            profileform.save()
            return redirect('accounts:profile', slug=profile.slug)
    else:
        userform = UserForm(instance=profile.user)
        profileform = ProfileForm(instance=profile)

        return render(request, 'account/profile_edit.html', {'userform': userform, 'profileform': profileform})

