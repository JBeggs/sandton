from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.template.response import TemplateResponse

from santon.forms import ContactForm


class IndexTemplateView(TemplateView):
    template_name = "santon/index.html"


class ServicesTemplateView(TemplateView):
    template_name = "santon/services.html"


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "santon/contact.html"
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        form.send_email()
        return TemplateResponse(
            self.request, self.template_name, {"success": True}
        )
