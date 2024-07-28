from django.contrib import admin
from .models import Book, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'des')
    list_per_page = 20
    search_fields = ['name']
admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ( "title", "author", 'image', 'price', 'sale','quantity','is_active','category' )
    search_fields = ["title", "author", "category__name"]
admin.site.register(Book, BookAdmin)