from django.http import Http404, HttpResponse
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


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
            user = form.save()
            current_site = get_current_site(request)
            mail_subject = 'An account is created'
            message = render_to_string('user_mail.html', {
                'user': user,
                'domain': current_site.domain
            })
            send_mail = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[send_mail])
            email.send()
            messages.success(request, "Send a mail")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('search')

    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            update = update_session_auth_hash(request, form.user)
            if update:
                messages.success(request, "Password Successfully changed")
                logout(request)
                return redirect('registration')
            else:
                messages.error(request, "Not updated")
        else:
            messages.error(request, "form not valid")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})
