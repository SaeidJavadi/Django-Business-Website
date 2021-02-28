from base.models import Footer, Header
from base.forms import NewslettersForm


def footerdata(request):
    data = Footer.objects.filter(status='active').last()
    return {'footer': data}


def headerdata(request):
    data = Header.objects.filter(status='active').last()
    return {'header': data}


def news(request):
    news = NewslettersForm()
    return {'news': news}
