from django.contrib import admin

from santon.apps.category.models import Category
from santon.apps.seo.admin import SEOGenericTabularInline


class CategoryModelAdmin(admin.ModelAdmin):
    model = Category
    inlines = [SEOGenericTabularInline]
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Category, CategoryModelAdmin)
