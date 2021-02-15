from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from accounts.forms import LoginForm
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from accounts.models import User


def userLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(email=cd['email']).exists():
                user = authenticate(request, username=cd['email'], password= cd['password'])
                if user is not None:
                    login(request, user)
                    messages.success(request, _('logged in successfully'), 'success')
                    return redirect('base:index')
                else:
                    messages.error(request, _('your Email Or Password is wrong'), 'warning')
            else:
                messages.error(request, _('No account created with this email'),
                               'warning')
                return redirect('accounts:login')
        else:
            messages.error(request, _('Please enter your information correctly'), 'warning')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})
