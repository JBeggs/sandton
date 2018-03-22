from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)

    class Meta(object):
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name
