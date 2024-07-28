from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['fname', 'lname', 'mobile', 'email', 'password', 'address']

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True) 

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if not email or not password:
            raise serializers.ValidationError('Email and password are required.')

        user = User.objects.filter(email=email).first()
        if user:
            if check_password(password, user.password):
                return user 
            else:
                raise serializers.ValidationError('Invalid password.')
        else:
            raise serializers.ValidationError('User does not exist.')

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not check_password(value, user.password):
            raise serializers.ValidationError('Incorrect old password.')
        return value

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'mobile', 'address']

    def update(self, instance, validated_data):
        instance.fname = validated_data.get('fname', instance.fname)
        instance.lname = validated_data.get('lname', instance.lname)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
