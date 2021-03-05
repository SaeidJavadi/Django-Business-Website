from random import randint
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from accounts.forms import LoginForm, RegisterForm, ForgetForm, ResetPassword, EditProfileForm, VerifyForm
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from accounts.models import User
from accounts.tasks import checkbirth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# from django.views import View
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.decorators.csrf import csrf_exempt, csrf_protect


def userLogin(request):
    if not request.user.is_active:
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
    else:
        return redirect('base:index')


def userRegister(request):
    if not request.user.is_active:
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
                                                                phone=cd['phone'], idcode=cd['idcode'],
                                                                password=cd['password1'])
                                user.save()
                                messages.success(request, _('you registered successfully'), 'success')
                                return redirect('accounts:login')
                            else:
                                messages.success(request, _('this idcode is exists'))
                        else:
                            messages.success(request, _('this phone is exists'))
                    else:
                        messages.success(request, _('People under the age of 18 are not allowed to register'),
                                         'warning')
                else:
                    messages.success(request, _('this Email is exists'), 'warning')
        return render(request, 'accounts/register.html', {'form': form})
    else:
        return redirect('base:index')


def LogoutPage(request):
    logout(request)
    messages.success(request, _('you logged out successfully'), 'success')
    return redirect('base:index')


def ForgetPage(request):
    if not request.user.is_active:
        if request.method == 'POST':
            form = ForgetForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                if User.objects.filter(email=cd['email'], idcode=cd['idcode']).exists():
                    request.session['email'] = cd['email']
                    request.session['idcode'] = cd['idcode']
                    return redirect('accounts:reset')
                else:
                    messages.error(request, _('No account created with this email and ID code'),
                                   'warning')
                    return redirect('accounts:forget')
        else:
            form = ForgetForm()
            return render(request, 'accounts/forget.html', {'form': form})
    else:
        return redirect('base:index')


def resetpass(request):
    if not request.user.is_active:
        if request.method == 'POST':
            form = ResetPassword(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = User.objects.get(email=request.session['email'], idcode=request.session['idcode'])
                user.set_password(cd['password1'])
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, _('Your password has been successfully changed'), 'success')
                return redirect('accounts:login')
        else:
            if request.session['email'] and request.session['idcode']:
                form = ResetPassword()
                return render(request, 'accounts/reset.html', {'form': form})
    else:
        return redirect('base:index')


@login_required()
def profile(request):
    user = User.objects.get(email=request.user.email)
    form = EditProfileForm(request.POST or None, instance=user)
    form_password = ResetPassword(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, _('updated successfully.'), extra_tags='alert alert-success')
            return redirect('accounts:profile')
        elif form_password.is_valid():
            cd = form_password.cleaned_data
            user.set_password(cd['password1'])
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password has been successfully changed'), 'success')
            logout(request)
            return redirect('accounts:login')
        else:
            # cd = form.cleaned_data
            # error = ''
            # if User.objects.filter(email=cd['email']).exists():
            #     error = 'ایمیلی که وارد کرده اید از قبل وجود دارد'
            # if User.objects.filter(email=cd['phone']).exists():
            #     error = 'شماره تلفنی که وارد کرده اید از قبل وجود دارد!!'
            # elif User.objects.filter(idcode=cd['idcode']).exists():
            #     error = 'کدملی که وارد کرده اید از قبل وجود دارد!!'
            messages.success(request, _('Error updating your profile!!'), extra_tags='warning')
            return redirect('accounts:profile')
    else:
        return render(request, 'accounts/profile.html', {'user':user, 'form': form, 'form_password':form_password})


@login_required()
def verify(request):
    user = User.objects.get(email=request.user.email)
    if request.method == 'POST':
        pass
    else:
        form = VerifyForm()
        code = randint(1000,9999)
        ## method send
        return render(request, 'accounts/verify.html', {'form':form})