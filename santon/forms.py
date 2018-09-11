from django import forms

from santon.utils import construct_choices, render_email_template, send_email


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=150,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    contact_number = forms.CharField(
        max_length=15,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email_address = forms.EmailField(widget=forms.widgets.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    closest_branch = forms.CharField(
        widget=forms.widgets.Select(
            choices=construct_choices(["Johannesburg", "Durban"])
        )
    )
    message = forms.CharField(max_length=1000, widget=forms.widgets.Textarea(
        attrs={
            "class": "form-control"
        }
    ))

    newsletter = forms.BooleanField(
        initial=True, label='I want to receive more news and updates from Santon Workwear'
    )

    def send_email(self):
        data = self.cleaned_data
        send_email(
            "[SANTON] Website Enquiry",
            render_email_template(
                "santon/emails/enquiry.txt", {
                    "data": data
                }
            ),
            to=["jhbsales@santonworkwear.co.za"],
            reply_to=["%s <%s>" % (data["full_name"], data["email_address"])]
        )
