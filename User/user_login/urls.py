from django.urls import path
from . import views

urlpatterns = [
    path('api/ecomSys/user/login/', views.LoginView.as_view(), name='login'),
    # path('a/', views.AView.as_view()), 
]
