from django.urls import path
from . import views

urlpatterns = [
    path('api/ecomSys/user/info/', views.UserInfoView.as_view(), name='user_detail'),
    path('api/ecomSys/user/change/', views.ChangePasswordView.as_view(), name='change'),
    path('api/ecomSys/user/update/', views.UpdateProfileView.as_view(), name='update'),
]
