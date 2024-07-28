# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework.views import APIView
import requests
import random
import requests
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


class GetAllProduct(APIView):
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
        all_products = random.sample(all_products, len(all_products))
        top_products = sorted(all_products, key=lambda x: x['sale'], reverse=True)[:4]
        
        return render(request, 'home.html', {'products': top_products})
    
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
        all_products = random.sample(all_products, len(all_products))
        numberPro = len(all_products)
        return render(request, 'shop.html', {'products': all_products, 'numberP': numberPro})

class LoginView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
            email = request.POST.get('email')
            password = request.POST.get('password')

            url = 'http://127.0.0.1:8000/api/ecomSys/user/login/'
            data = {
                'email': email,
                'password': password
            }
            try:
                response = requests.post(url, data=data)
                if response.status_code == 200:
                    json_data = response.json()
                    user_info = json_data['user']
                    access_token = json_data['access']
                    refresh_token = json_data['refresh']

                    # Lưu thông tin người dùng vào session
                    request.session['user_info'] = user_info
                    request.session['access_token'] = access_token
                    request.session['refresh_token'] = refresh_token

                    return redirect('home')  
                else:
                    return render(request, 'login.html', {'error': 'Login failed. Please try again.'})

            except Exception as e:
                return render(request, 'login.html', {'error': 'Login failed. Please try again.'})
            
class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        url = 'http://127.0.0.1:8000/api/ecomSys/user/register/'

        try:
            response = requests.post(url, data=request.data)
            if response.status_code == 201: 
                email = request.data['email'] 
                password = request.data['password'] 
                return render(request, 'login.html', {'email1': email, 'password1': password})
            else:
                email = request.data['email']          
                print("----------------------------------")
                data_without_email = {key: value for key, value in request.data.items() if key != 'email'}
                return render(request, 'signup.html', {'error': 'Email already exists. Please use a different email.', 'formData': data_without_email})

        except Exception as e:
            return render(request, 'signup.html', {'error': 'Email already exists. Please use a different email.'})         
            
class LogoutView(APIView):
    def get(self, request):
        if 'user_info' in request.session:
            del request.session['user_info']
        if 'access_token' in request.session:
            del request.session['access_token']
        if 'refresh_token' in request.session:
            del request.session['refresh_token']
        return redirect('home')           
            
class GetAllBook(APIView):
    def get(self,  request):
        books_api = "http://127.0.0.1:8002/api/product/book/all/"
        response_books = requests.get(books_api)
        if response_books.status_code == 200:
            books_data = response_books.json()
        else:
            books_data = []
            
        all_products = books_data
        all_products = random.sample(all_products, len(all_products))
        numberPro = len(all_products)
        return render(request, 'shopBook.html', {'products': all_products, 'numberP': numberPro}) 
    
class GetAllCategory(APIView):
    def get(self, request):
        url = "http://127.0.0.1:8002/api/product/category/all/"   
    
class GetAllMobiles(APIView):
    def get(self,  request):
        mobiles_api = "http://127.0.0.1:8002/api/product/mobile/all/"

        response_mobiles = requests.get(mobiles_api)
        if response_mobiles.status_code == 200:
            mobiles_data = response_mobiles.json()
        else:
            mobiles_data = []

        all_products = mobiles_data
        all_products = random.sample(all_products, len(all_products))
        numberPro = len(all_products)
        return render(request, 'shopMobiles.html', {'products': all_products, 'numberP': numberPro})           

# class AddToCart(APIView):
    