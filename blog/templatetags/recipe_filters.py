from django import template
from django.utils import timezone

register = template.Library()

# Truncate Length of Text on Home Page
@register.filter
def truncate_text(value, max_length):
    if len(value) <= max_length:
        return value
    return value[:max_length] + ' . . .'

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