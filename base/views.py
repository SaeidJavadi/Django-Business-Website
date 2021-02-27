from django.shortcuts import render, redirect
from base.models import About, Services, Contact
from base.forms import ContactForm
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
            messages.success(request, _('updated successfully!!'), extra_tags='alert alert-success')
            return redirect('base:contact')
    else:
        form = ContactForm()
    return render(request, template_name='base/contact.html', context={'form': form})
