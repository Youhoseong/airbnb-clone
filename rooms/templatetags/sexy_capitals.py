from django import template



# example making filter

register = template.Library()

@register.filter # decorator
def sexy_capitals(value):
    print(value)
    return 'lalalalalala'