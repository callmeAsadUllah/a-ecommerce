from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)

from .models import (
    ProductModel,
    ProductImageModel
)


class HomeListView(ListView, object):
    context_object_name = 'products'
    model = ProductModel
    template_name = 'mainapp/home.html'


class DeliveryTemplateView(TemplateView, object):
    template_name = 'mainapp/delivery.html'


class PaymentTemplateView(TemplateView, object):
    template_name = 'mainapp/payment.html'


class IndexTemplateView(TemplateView, object):
    template_name = 'mainapp/index.html'

