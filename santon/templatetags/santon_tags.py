from django import template
from django.core.urlresolvers import NoReverseMatch, reverse

from santon.utils import image_resize


register = template.Library()


@register.simple_tag(takes_context=True)
def get_active_link(context, pattern):
    """Add an active class to links that are in focus.
    """
    try:
        url = reverse(pattern)
    except NoReverseMatch:
        return ""
    request = context.get("request")
    if request:
        if url == "/":
            if url == request.path:
                return "active"
        elif url in request.path:
            return "active"
    return ""


@register.simple_tag
def resize_image(image, width=None, height=None):
    return image_resize(image, width, height)
