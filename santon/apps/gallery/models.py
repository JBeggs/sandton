from __future__ import unicode_literals

from django.db import models


class Gallery(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta(object):
        verbose_name_plural = "Galleries"

    def __unicode__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/%Y/%m/")
    gallery = models.ForeignKey(
        Gallery, related_name="images", blank=True, null=True
    )
