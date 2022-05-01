import csv

from django.http import HttpResponse
from django.views.generic.list import ListView
from product.models import Product


def upload_data(request):
    with open('viatec.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            try:
                created = Product.objects.get_or_create(
                    product_name=row[0],
                    product_description=row[1],
                    price=row[2],
                    url=row[3],
                )
            except:
                pass
    return HttpResponse('Done!')


class FilterView(ListView):
    template_name = 'product_table.html'
    queryset: object = Product.objects.filter(price__contains="1833.0")


class ExcludeView(ListView):
    template_name = 'product_table.html'
    queryset = Product.objects.exclude(product_name__contains='камера')


class OrderByView(ListView):
    template_name = 'product_table.html'
    queryset = Product.objects.exclude(product_name__contains='HDCVI видеокамера').order_by('price')


class AllView(ListView):
    template_name = 'product_table.html'
    queryset = Product.objects.all()


class UnionView(ListView):
    template_name = 'product_table.html'
    queryset = Product.objects.filter(product_name='1200').union(Product.objects.filter(product_name='HDCVI'))
