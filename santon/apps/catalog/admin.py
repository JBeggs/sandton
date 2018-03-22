from django.contrib import admin

from santon.apps.catalog.models import Brand, Colour, Fabric, Product, Size
from santon.apps.seo.admin import SEOGenericTabularInline


def publish(modeladmin, request, queryset):
    queryset.update(published=True)


def unpublish(modeladmin, request, queryset):
    queryset.update(published=False)


class BrandModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


class ProductModelAdmin(admin.ModelAdmin):
    actions = [publish, unpublish]
    list_display = ["name", "published"]
    list_display_links = ["name"]
    inlines = [SEOGenericTabularInline]
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Brand, BrandModelAdmin)
admin.site.register(Colour)
admin.site.register(Fabric)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Size)
