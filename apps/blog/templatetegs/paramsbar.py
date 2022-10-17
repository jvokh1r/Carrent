from django.template import Library
from ..models import Tag, Category

register = Library()


@register.simple_tag
def params_categories():
    return Category.objects.all()


@register.simple_tag
def params_tags():
    return Tag.objects.all()