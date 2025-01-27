from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user_model.models import User
from user_model.authentication import SafeJWTAuthentication
from user_model.utils import generate_access_token, generate_refresh_token
from .serializers import UserInfoSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect


class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        email = request.data['email']          
        existing_user = User.objects.filter(email=email).first()
        if existing_user:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():            
            user = serializer.save()
            access_token = generate_access_token(user)
            refresh_token = generate_refresh_token(user)

            user_serializer = UserInfoSerializer(user)
      
            return Response({
                'user': user_serializer.data,
                'refresh': refresh_token,
                'access': access_token,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyTokenView(APIView):
    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'message': 'Token is valid.'}, status=status.HTTP_200_OK)