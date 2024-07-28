from django.urls import path
from . import views

urlpatterns = [
    path('api/product/category/add/', views.CreateCategoryView.as_view()),
    path('api/product/book/add/', views.AddBookView.as_view()),
    path('api/product/category/all/', views.CategoryListView.as_view()),
    path('api/product/book/all/', views.BookListView.as_view()),
    path('api/product/book/detail/<str:id>/', views.BookDetailView.as_view()),
    path('api/product/book/category/<str:id>/', views.BookListofCategoryView.as_view()),
    path('api/product/book/search/<str:key>/', views.SearchBookListView.as_view()),
    path('api/product/book/edit/<str:id>/', views.UpdateBookView.as_view()),
    path('api/product/book/delete/<str:id>/', views.DeleteBook.as_view()),
    path('api/product/category/delete/<str:id>/', views.DeleteCategory.as_view()),
]

