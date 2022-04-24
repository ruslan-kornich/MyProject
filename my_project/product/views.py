from decimal import Decimal
from uuid import uuid4

from django.http import HttpResponse
from product.models import Product, Client
from django.core.files import File


def create_product(request):
    camera = Product()
    camera.count = 5
    camera.product_description = "2Мп Starlight IP видеокамера с ИК подсветкой" \
                                 "Матрица: 1/2.7 progressive CMOS " \
                                 "Функции: видео аналитика (IVS)"
    camera.url = 'https://viatec.ua/ru/product/DH-IPC-HDW2230TP-AS-S2-28'
    camera.name = "DH-IPC-HDW2230TP-AS-S2 (2.8 мм)"
    camera.save()
    return HttpResponse('Created!')


def create_client(request):
    client = Client.objects.create(**{
        'second_email': 'admin@admin1.com',
        'name': 'MyName',
        'invoice': File(open('requirements.txt')),
        'user_uuid': uuid4(),
        'discount_size': Decimal('0.00052'),
        'client_ip': '192.168.1.100',
    })
    return HttpResponse("Created")


def get_camera(request):
    price = Product.shop.get(id=1).price
    return HttpResponse(price)
