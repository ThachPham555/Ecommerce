import requests
from djongo.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Book
from .serializers import CategorySerializer, BookSerializer, BookInfoSerializer, UpdateBookSerializer


class CreateCategoryView(APIView):
    def post(self, request):
        # token_verification_url = "http://localhost:8001/api/ecomSys/manager/verify-token/"
        # headers = {'Authorization': request.headers.get('Authorization')}
        # response = requests.get(token_verification_url, headers=headers)
        
        # if response.status_code == 200:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)
    
class AddBookView(APIView):
    def post(self, request):
        # token_verification_url = "http://localhost:8001/api/ecomSys/manager/verify-token/"
        # headers = {'Authorization': request.headers.get('Authorization')}
        # response = requests.get(token_verification_url, headers=headers)
        
        # if response.status_code == 200:
            print(request.data)
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.filter(is_active__in=[True]).all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookListView(APIView):
    def get(self, request):
        books = Book.objects.filter(is_active__in=[True]).all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookListofCategoryView(APIView):
    def get(self, request, id):
        books = Book.objects.filter(category=id, is_active__in=[True])
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SearchBookListView(APIView):
    def get(self, request, key):
        books = Book.objects.filter(Q(title__icontains=key) | Q(author__icontains=key), is_active__in=[True])
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateBookView(APIView):
    def put(self, request, book_id):
        token_verification_url = "http://localhost:8001/api/ecomSys/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        
        if response.status_code == 200:
            try:
                book = Book.objects.get(id=book_id)
            except Book.DoesNotExist:
                return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UpdateBookSerializer(book, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class DeleteCategory(APIView):
    def delete(self, request, id):
        token_verification_url = "http://localhost:8001/api/ecomSys/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)

        if response.status_code == 200:
            try:
                category = Category.objects.get(id=id)
            except Category.DoesNotExist:
                return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = CategorySerializer()
            serializer.destroy(category)
            
            return Response({'message': 'Category soft deleted'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)


class DeleteBook(APIView):
    def delete(self, request, id):
        token_verification_url = "http://localhost:8001/api/ecomSys/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)

        if response.status_code == 200:
            try:
                book = Book.objects.get(id=id)
                print(book)
            except Book.DoesNotExist:
                return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = BookSerializer()
            serializer.destroy(book)

            return Response({'message': 'Book soft deleted'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class BookDetailView(APIView):
    def get(self, request, id):
        book = Book.objects.filter(id=id, is_active__in=[True]).first()
        serializer = BookInfoSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)