from django import template
from accounts.models import User
from django.template.loader import get_template

register = template.Library()


@register.filter()
def makerange(number):
    return range(number)


@register.simple_tag()
def usercounter():
    return User.objects.all().count()


