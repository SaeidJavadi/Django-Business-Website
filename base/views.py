from django.shortcuts import render, redirect
from base.models import About, Services
from base.forms import ContactForm, NewslettersForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def index(request):
    return render(request, template_name='base/index.html', context={})


def about(request):
    about = About.objects.filter(status='active').last()
    return render(request, template_name='base/about.html', context={'about': about})


def services(request):
    service = Services.objects.filter(status='active').last()
    return render(request, template_name='base/services.html', context={'service': service})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message has been successfully sent'), extra_tags='alert alert-success')
            return redirect('base:contact')
        else:
            messages.success(request, _('An error occurred while sending your message'),
                             extra_tags='alert alert-warning')
    else:
        form = ContactForm()
    return render(request, template_name='base/contact.html', context={'form': form})


def newsletters(request):
    if request.method == 'POST':
        form = NewslettersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your email was successfully added to the newsletter'),
                             extra_tags='alert alert-success')
            return redirect('base:index')
