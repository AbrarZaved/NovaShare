from django import template

register = template.Library()


@register.filter
def basename(value):
    extension = value.split('.')[-1]
    base = value.replace(f'.{extension}', '')
    return base[6:65] + f'.{extension}' 
