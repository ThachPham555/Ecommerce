from django.urls import path
from . import views

urlpatterns = [
    path('home', views.GetAllProduct.as_view(), name='home'),
    path('shop', views.GetAllShop.as_view(), name='shop'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterUserView.as_view(), name='register'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('books', views.GetAllBook.as_view(), name='books'),
    path('mobiles', views.GetAllMobiles.as_view(), name='mobiles'),
]
