from django.conf.urls import url

from santon.apps.catalog import views


urlpatterns = [
    url(
        r"^category/(?P<category_slug>[-\w]+)/",
        views.ProductListView.as_view(),
        name="category_list"
    ),
    url(
        r"^(?P<slug>[-\w]+)/$",
        views.ProductDetailView.as_view(),
        name="detail"
    ),

]
