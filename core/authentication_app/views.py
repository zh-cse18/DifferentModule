from django.http import Http404, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'blog-listing.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('search')
    else:
        if request.method == 'POST':
            user = request.POST.get('user')
            password = request.POST.get('password')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('search')
    return render(request, 'login.html', )


def user_logout(request):
    logout(request)
    return redirect('search')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('search')

    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})



