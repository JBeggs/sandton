from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class SEO(models.Model):
    """
    A simple SEO model which points to a generic foreign key.
    """
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=160)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta(object):
        verbose_name = "SEO"
        verbose_name_plural = "SEO"

    def __unicode__(self):
        return self.title
