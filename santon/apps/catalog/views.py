from django.views.generic import DetailView, ListView

from santon.apps.catalog.models import Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super(
            ProductListView, self
        ).get_queryset().filter(published=True)

        category_slug = self.kwargs.get("category_slug")
        if category_slug is not None:
            queryset = queryset.filter(categories__slug=category_slug)
        return queryset


class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):
        return super(
            ProductDetailView, self
        ).get_queryset().filter(published=True)
