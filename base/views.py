from django.shortcuts import render
from base.models import About


def index(request):
    return render(request, template_name='base/index.html', context={})


def about(request):
    about = About.objects.filter(status='active').last()
    return render(request, template_name='base/about.html', context={'about': about})


def services(request):
    return render(request, template_name='base/services.html', context={})


def contact(request):
    return render(request, template_name='base/contact.html', context={})
