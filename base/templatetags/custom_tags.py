from django import template

register = template.Library()


@register.filter()
def makeRange(Number):
    return range(Number)
