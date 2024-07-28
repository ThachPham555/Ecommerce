from django.urls import path
from . import views

urlpatterns = [
    path('api/ecomSys/user/register/', views.RegisterView.as_view(), name='register'),
    path('api/ecomSys/user/verify-token/', views.VerifyTokenView.as_view(), name='verify_token'),
]
