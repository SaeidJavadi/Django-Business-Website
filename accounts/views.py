from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from accounts.forms import LoginForm, RegisterForm, ForgetForm
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from accounts.models import User
from accounts.tasks import checkbirth


def userLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(email=cd['email']).exists():
                user = authenticate(request, username=cd['email'], password=cd['password'])
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


def userRegister(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            birth = cd['dateofbirth']
            if not User.objects.filter(email=cd['email']).exists():
                if checkbirth(birth):
                    if not User.objects.filter(phone=cd['phone']).exists():
                        if not User.objects.filter(idcode=cd['idcode']).exists():
                            user = User.objects.create_user(email=cd['email'], full_name=cd['full_name'],
                                                            dateofbirth=cd['dateofbirth'],
                                                            phone=cd['phone'], idcode=cd['idcode'], password=cd['password1'])
                            user.save()
                            messages.success(request, _('you registered successfully'), 'success')
                            return redirect('accounts:login')
                        else:
                            messages.success(request,_('this idcode is exists'))
                    else:
                        messages.success(request,_('this phone is exists'))
                else:
                    messages.success(request, _('People under the age of 18 are not allowed to register'), 'warning')
            else:
                messages.success(request, _('this Email is exists'),'warning')
    return render(request, 'accounts/register.html', {'form': form})


def LogoutPage(request):
    logout(request)
    messages.success(request, _('you logged out successfully'), 'success')
    return redirect('base:index')


def ForgetPage(request):
    if request.method == 'POST':
        form = ForgetForm(request.POST)
        pass
    else:
        form = ForgetForm()
    return render(request, 'accounts/forget.html', {'form': form})
