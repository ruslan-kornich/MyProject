from django.views.generic import CreateView
from product.models import Product, Supplier, Contact
from rest.serializers import ProductModelSerializer, SupplierModelSerializer
from rest_framework import viewsets
from rest.forms import ContactForm
from rest.service import send
from .tasks import send_spam_email







class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/rest/contact/'
    template_name = 'rest/contact.html'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)
