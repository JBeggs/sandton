from django.contrib import admin

from santon.apps.gallery.models import Gallery, Image
from santon.apps.seo.admin import SEOGenericTabularInline


class ImageTabularInline(admin.TabularInline):
    model = Image
    min_num = 1
    extras = 5


class GalleryModelAdmin(admin.ModelAdmin):
    model = Gallery
    inlines = [SEOGenericTabularInline, ImageTabularInline]
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Gallery, GalleryModelAdmin)
