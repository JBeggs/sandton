from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from colorfield.fields import ColorField

from santon import utils
from santon.apps.category.models import Category
from santon.apps.gallery.models import Gallery
from santon.apps.seo.models import SEO


class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta(object):
        ordering = ["name"]

    def __unicode__(self):
        return self.name


class Fabric(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Colour(models.Model):
    name = models.CharField(max_length=50)
    colour = ColorField(default="#000000")

    def __unicode__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(
        max_length=10, help_text="Use short name, e.g. XXL"
    )

    def __unicode__(self):
        return self.size


class Product(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    position = models.PositiveIntegerField(default=0)

    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    blurb = models.TextField()

    weight = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    unit_of_weight = models.CharField(
        max_length=10,
        choices=utils.construct_choices(
            settings.SANTON_CONFIG["UNIT_OF_WEIGHT"]
        ), blank=True, null=True
    )
    fabric = models.ForeignKey(Fabric)
    brands = models.ManyToManyField(Brand)
    colours = models.ManyToManyField(Colour)
    sizes = models.ManyToManyField(Size)

    categories = models.ManyToManyField(Category)
    gallery = models.ForeignKey(Gallery, blank=True, null=True)

    seo = GenericRelation(SEO)

    class Meta(object):
        ordering = ["position"]

    def __unicode__(self):
        return self.name

    @property
    def size_str(self):
        return ", ".join(size.size for size in self.sizes.all())

    @property
    def brand_str(self):
        return ", ".join(brand.name for brand in self.brands.all())

    @property
    def thumbnail(self):
        try:
            return getattr(self.gallery.images.first(), "image", None)
        except AttributeError:
            pass
