from django.views.generic import CreateView
from product.models.Contact import Contact
from rest.forms import ContactForm
from rest.tasks import send_spam_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/rest/contact/'
    template_name = 'rest/contact.html'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)
