from django import template
from django.utils.safestring import mark_safe
import CommonMark

register = template.Library()


@register.filter()
def markdown(text):
    parser = CommonMark.DocParser()
    renderer = CommonMark.HTMLRenderer()

    ast = parser.parse(text)
    return mark_safe(renderer.render(ast))