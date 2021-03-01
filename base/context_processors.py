from base.models import Footer, Header
from base.forms import NewslettersForm


def footerdata(request):
    data = Footer.objects.filter(status='active').last()
    logo = str(data.logo).replace('..', '')
    return {'footer': data, 'logo': logo}


def headerdata(request):
    data = Header.objects.filter(status='active').last()
    logo = str(data.logo).replace('..', '')
    return {'header': data, 'logo': logo}


def news(request):
    news = NewslettersForm()
    return {'news': news}
