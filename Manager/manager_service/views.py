from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from manager_service.authentication import SafeJWTAuthentication
from manager_service.utils import generate_access_token, generate_refresh_token
from .serializers import  ManagerInfoSerializer, ManagerLoginSerializer, ManagerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

class AddManagerView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            manager = serializer.save()
            access_token = generate_access_token(manager)
            refresh_token = generate_refresh_token(manager)

            manager_serializer = ManagerInfoSerializer(manager)

            return Response({
                'manager': manager_serializer.data,
                'refresh': refresh_token,
                'access': access_token,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = ManagerLoginSerializer(data=request.data)
        if serializer.is_valid():
            manager = serializer.validated_data  
            access_token = generate_access_token(manager)
            refresh_token = generate_refresh_token(manager)

            manager_serializer = ManagerInfoSerializer(manager)
            
            return Response({
                'manager': manager_serializer.data,
                'refresh': refresh_token,
                'access': access_token,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManagerInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        manager = request.user
        serializer = ManagerInfoSerializer(manager)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VerifyTokenView(APIView):
    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'message': 'Token is valid.'}, status=status.HTTP_200_OK)