from django.urls import path
from . import views

urlpatterns = [
    path('api/ecomSys/manager/add/', views.AddManagerView.as_view(), name='register'),
    path('api/ecomSys/manager/login/', views.LoginView.as_view(), name='login'),
    path('api/ecomSys/manager/info/', views.ManagerInfoView.as_view(), name='manager-detail'),
    path('api/ecomSys/manager/verify-token/', views.VerifyTokenView.as_view(), name='verify-token'),
]

