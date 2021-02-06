from django.shortcuts import render

def index(request):
    return render(request, template_name='base/index.html', context={})


def about(request):
    return render(request, template_name='base/about.html',context={})


def services(request):
    return render(request, template_name='base/services.html',context={})


def contact(request):
    return render(request, template_name='base/contact.html', context={})