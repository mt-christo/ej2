from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def cescape(value, arg):
    return value.replace("&ie&", arg)


@register.filter
@stringfilter
def iescape(value):
    return value.replace("39;", "'")
