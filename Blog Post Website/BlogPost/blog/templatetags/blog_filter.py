from django import template

register = template.Library()

@register.filter
def rm_period(value):
    return value.replace('.', '')