# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework.views import APIView
import requests
import random

class GetAllProduct(APIView):
    def get(self,  request):
        return render(request,"http://127.0.0.1:8002/shop")
    
class GetAllShop(APIView):
    def get(self,  request):
        mobiles_api = "http://127.0.0.1:8002/api/product/mobile/all/"
        books_api = "http://127.0.0.1:8002/api/product/book/all/"

        response_mobiles = requests.get(mobiles_api)
        if response_mobiles.status_code == 200:
            mobiles_data = response_mobiles.json()
        else:
            mobiles_data = []

        response_books = requests.get(books_api)
        if response_books.status_code == 200:
            books_data = response_books.json()
        else:
            books_data = []
            
        all_products = mobiles_data + books_data
        print(all_products)
        for a in all_products:
            a['image'] = "/Ecom/Product" + a['image']
        all_products = random.sample(all_products, len(all_products))
        numberPro = len(all_products)
        return render(request, 'shop.html', {'products': all_products, 'numberP': numberPro})

