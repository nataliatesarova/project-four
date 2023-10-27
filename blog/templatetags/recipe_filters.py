from django import template

register = template.Library()

# Truncate text length
@register.filter
def truncate_text(value, max_length):
    if len(value) <= max_length:
        return value
    return value[:max_length] + ' . . .'
