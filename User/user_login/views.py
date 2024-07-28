from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user_model.utils import generate_access_token, generate_refresh_token
from user_model.serializers import UserInfoSerializer, UserLoginSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
     
        
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data  
            access_token = generate_access_token(user)
            refresh_token = generate_refresh_token(user)

            user_serializer = UserInfoSerializer(user)
            return Response({
                'user': json.dumps(user_serializer.data),
                'refresh': refresh_token,
                'access': access_token,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    