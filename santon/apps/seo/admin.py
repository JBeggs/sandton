from django.contrib.contenttypes.admin import GenericTabularInline

from santon.apps.seo.models import SEO


class SEOGenericTabularInline(GenericTabularInline):
    model = SEO
    max_num = 1
    extras = 1
