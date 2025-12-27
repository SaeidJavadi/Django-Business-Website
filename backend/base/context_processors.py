from base.models import Footer, Header
from base.forms import NewslettersForm


def footerdata(request):
    data = Footer.objects.filter(status='active').last()
    if data and data.logo:
        logo = str(data.logo).replace('..', '')
    else:
        logo = None
    return {'footer': data, 'logo': logo}


def headerdata(request):
    data = Header.objects.filter(status='active').last()
    if data and data.logo:
        logo = str(data.logo).replace('..', '')
    else:
        logo = None
    return {'header': data, 'logo': logo}


def news(request):
    news = NewslettersForm()
    return {'news': news}
