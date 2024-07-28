from django.urls import path
from . import views

urlpatterns = [
    path('api/product/brand/add/', views.CreateBrandView.as_view()),
    path('api/product/mobile/add/', views.AddMobileView.as_view()),
    path('api/product/brand/all/', views.BrandListView.as_view()),
    path('api/product/mobile/all/', views.MobileListView.as_view()),
    path('api/product/mobile/detail/<str:id>/', views.MobileDetailView.as_view()),
    path('api/product/mobile/brand/<str:id>/', views.MobileListofBrandView.as_view()),
    path('api/product/mobile/search/<str:key>/', views.SearchMobileListView.as_view()),
    path('api/product/mobile/edit/<str:id>/', views.UpdateMobileView.as_view()),
    path('api/product/mobile/delete/<str:id>/', views.DeleteMobile.as_view()),
    path('api/product/brand/delete/<str:id>/', views.DeleteBrand.as_view()),
]

