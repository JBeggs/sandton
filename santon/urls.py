from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from santon import views


urlpatterns = [
    url(r"^$", views.IndexTemplateView.as_view(), name="index"),
    url(r"^services/$", views.ServicesTemplateView.as_view(), name="services"),
    url(r"^contact/$", views.ContactFormView.as_view(), name="contact"),
    url(
        r"^products/",
        include("santon.apps.catalog.urls", namespace="catalog")
    ),
    url(r'^news/', include('newsapp.urls')),
    url(r"^admin/", admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
]

urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )



if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
