from django import template
from django.core import signing
from django.utils.html import format_html

register = template.Library()

@register.simple_tag(takes_context=True)
def h_csrf_token(context):
    csrf_field = signing.dumps('csrfmiddlewaretoken').partition(':')[0]
    return format_html("<input type='hidden' name='{0}' value='{1}' />", csrf_field, context['csrf_token'])
    # csrf_field = signing.dumps('csrfmiddlewaretoken').partition(':')[0]
    # return value.replace('csrfmiddlewaretoken',csrf_field)
