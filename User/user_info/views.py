from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user_model.authentication import SafeJWTAuthentication
from user_model.serializers import ChangePasswordSerializer, UpdateProfileSerializer, UserInfoSerializer
from rest_framework.permissions import IsAuthenticated

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SafeJWTAuthentication]

    def get(self, request):
        user = request.user
        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        serializer = UpdateProfileSerializer(instance=request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)