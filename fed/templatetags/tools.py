from django import template
register = template.Library()

@register.filter
def restar(value, arg):
    print arg
    return int(value)-int(arg)

@register.filter
def total_dict(value):    
    return sum(value.values())
        