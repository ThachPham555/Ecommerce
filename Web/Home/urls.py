from django.urls import path
from . import views

urlpatterns = [
    path('home', views.GetAllProduct.as_view(), name='get_all_products'),
    path('shop', views.GetAllShop.as_view(), name='shop'),
]
