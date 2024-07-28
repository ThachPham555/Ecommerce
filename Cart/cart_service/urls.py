from django.urls import path
from . import views

urlpatterns = [
    path('api/ecomSys/cart/add/', views.AddToCartView.as_view()),
    path('api/ecomSys/cart/show/', views.CartView.as_view()),
    path('api/ecomSys/cart/delete/<str:product_id>/', views.DeleteCartItemView.as_view()),
]

