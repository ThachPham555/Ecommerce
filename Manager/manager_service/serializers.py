from rest_framework import serializers
from .models import Manager
from django.contrib.auth.hashers import make_password, check_password

class ManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Manager
        fields = ['fname', 'lname', 'mobile', 'email', 'password', 'address']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

class ManagerLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True) 

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if not email or not password:
            raise serializers.ValidationError('Email and password are required.')

        user = Manager.objects.filter(email=email).first()
        if user:
            if check_password(password, user.password):
                return user 
            else:
                raise serializers.ValidationError('Invalid password.')
        else:
            raise serializers.ValidationError('Manager does not exist.')

class ManagerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

