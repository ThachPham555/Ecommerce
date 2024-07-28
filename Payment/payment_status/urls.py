from django.urls import path
from . import views

urlpatterns = [
    path('payment_status', views.user_transaction_info, name='payment_status'),
    path('payment_update', views.get_payment , name='payment_update'),
    path('pu', views.paymentUpdate, name='pu')
]
