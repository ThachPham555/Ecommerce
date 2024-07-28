from django.contrib import admin
from .models import Mobile, Brand
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'des')
    list_per_page = 20
    search_fields = ['name']
admin.site.register(Brand, BrandAdmin)


class MobileAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher", 'image', 'price', 'sale','quantity','is_active','brand' )
    search_fields = ["title", "publisher", "brand__name"]
admin.site.register(Mobile, MobileAdmin)