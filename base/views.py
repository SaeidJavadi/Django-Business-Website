from django.shortcuts import render
from base.models import About
from django.views.generic import DetailView


def index(request):
    return render(request, template_name='base/index.html', context={})


def about(request):
    about = About.objects.all().filter(status='active')[:1]
    for a in about:
        return render(request, template_name='base/about.html', context={'about': a})



def services(request):
    return render(request, template_name='base/services.html', context={})


def contact(request):
    return render(request, template_name='base/contact.html', context={})
