from django import template

from santon.apps.catalog.models import Product
from santon.apps.category.models import Category


register = template.Library()


@register.assignment_tag
def get_catalog_category_list(featured=False):
    """Return a unique list of categories associated to catalogs.
    """
    category_list = Category.objects.filter(pk__in=Product.objects.values_list(
        "categories", flat=True
    ).distinct())
    if featured:
        category_list = category_list.filter(featured=True)[:3]
    return category_list


@register.assignment_tag
def get_first_product(category_slug=None):
    """Return the first product given a category.
    """
    product_list = Product.objects.filter(
        published=True, gallery__images__isnull=False
    )
    if category_slug:
        product_list = product_list.filter(categories__slug=category_slug)
    return product_list.first()


@register.assignment_tag
def get_related_products(obj):
    """Return the first product given a category.
    """
    return Product.objects.filter(
        published=True, categories=obj.categories.first()
    ).exclude(pk=obj.pk)[:4]
