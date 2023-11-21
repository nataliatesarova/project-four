from django import template
from django.utils import timezone
import re

register = template.Library()

# Truncate Length of Text on Home Page
@register.filter
def truncate_text(value, max_length):
    if len(value) <= max_length:
        return value
    return value[:max_length] + ' . . .'

# Truncate after first line.
@register.filter
def first_sentence(value):
    # Finding the first sentence with Regular Expression
    match = re.search(r'(?<=[.!?])\s+', value)
    if match:
        return value[:match.start()]
    else:
        return value

# Date and time Filter for Comments
@register.filter
def format_comment_date(comment, recipe):
    now = timezone.now()
    comment_age = now - comment.created_on
    
    if comment_age.days < 0:
        return comment.created_on.strftime("%F %d, %Y")
    elif comment_age.days < 1:
        return "Today"
    elif comment_age.days == 1:
        return "Yesterday"
    else:
        return comment.created_on.strftime("%b %d ")