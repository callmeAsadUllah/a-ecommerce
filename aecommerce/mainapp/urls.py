from django.urls import path

from .views import (
    IndexTemplateView,
    HomeListView,
    DeliveryTemplateView,
    PaymentTemplateView
)

app_name = 'main'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index_view'),
    path('home/', HomeListView.as_view(), name='home_view'),
    path('payment/', PaymentTemplateView.as_view(), name='payment_view'),
    path('delivery/', DeliveryTemplateView.as_view(), name='delivery_view')
]
