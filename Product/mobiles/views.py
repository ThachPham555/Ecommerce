import requests
from djongo.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Brand, Mobile
from .serializers import BrandSerializer, MobileSerializer, MobileInfoSerializer, UpdateMobileSerializer

class CreateBrandView(APIView):
    def post(self, request):
        token_verification_url = "http://localhost:4001/api/ecomSys/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        
        if response.status_code == 200:
            serializer = BrandSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)
    
class AddMobileView(APIView):
    def post(self, request):
        token_verification_url = "http://localhost:4001/api/ecomSys/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        
        if response.status_code == 200:
            serializer = MobileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class BrandListView(APIView):
    def get(self, request):
        categories = Brand.objects.filter(is_active__in=[True]).all()
        serializer = BrandSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MobileListView(APIView):
    def get(self, request):
        mobiles = Mobile.objects.filter(is_active__in=[True]).all()
        serializer = MobileInfoSerializer(mobiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MobileListofBrandView(APIView):
    def get(self, request, id):
        mobiles = Mobile.objects.filter(brand=id, is_active__in=[True])
        serializer = MobileInfoSerializer(mobiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SearchMobileListView(APIView):
    def get(self, request, key):
        mobiles = Mobile.objects.filter(Q(title__icontains=key) | Q(publisher__icontains=key), is_active__in=[True])
        serializer = MobileInfoSerializer(mobiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateMobileView(APIView):
    def put(self, request, id):
        token_verification_url = "http://localhost:4001/api/ecomSys/manager/verify-token/"
        headers = {'Authorization': request.headers.get('Authorization')}
        response = requests.get(token_verification_url, headers=headers)
        
        if response.status_code == 200:
            try:
                mobile = Mobile.objects.get(id=id)
            except Mobile.DoesNotExist:
                return Response({'error': 'Mobile not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UpdateMobileSerializer(mobile, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class DeleteBrand(APIView):
    def delete(self, request, id):
        # token_verification_url = "http://localhost:4001/api/ecomSys/manager/verify-token/"
        # headers = {'Authorization': request.headers.get('Authorization')}
        # response = requests.get(token_verification_url, headers=headers)

        # if response.status_code == 200:
            try:
                brand = Brand.objects.get(id=id)
            except Brand.DoesNotExist:
                return Response({'error': 'Brand not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = BrandSerializer()
            serializer.destroy(brand)
            
            return Response({'message': 'Brand soft deleted'}, status=status.HTTP_204_NO_CONTENT)

        # return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)


class DeleteMobile(APIView):
    def delete(self, request, id):
        # token_verification_url = "http://localhost:4001/api/ecomSys/manager/verify-token/"
        # headers = {'Authorization': request.headers.get('Authorization')}
        # response = requests.get(token_verification_url, headers=headers)

        # if response.status_code == 200:
            try:
                mobile = Mobile.objects.get(id=id)
                print(mobile)
            except Mobile.DoesNotExist:
                return Response({'error': 'Mobile not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = MobileSerializer()
            serializer.destroy(mobile)

            return Response({'message': 'Mobile soft deleted'}, status=status.HTTP_204_NO_CONTENT)

        # return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)

class MobileDetailView(APIView):
    def get(self, request, id):
        mobile = Mobile.objects.filter(id=id, is_active__in=[True]).first()
        serializer = MobileInfoSerializer(mobile)
        return Response(serializer.data, status=status.HTTP_200_OK)