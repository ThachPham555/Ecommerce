from rest_framework import serializers
from .models import Category, Book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id' ,'name', 'des']
        
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class BookSerializer(serializers.ModelSerializer):
    category = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'type' ,'image', 'price', 'sale', 'quantity', 'des', 'category']

    def create(self, validated_data):
        print(validated_data)
        category = validated_data.pop('category', None)
        print(category)

        if category:
            category_instance = Category.objects.filter(is_active__in=[True], id=category).first()
            validated_data['category'] = category_instance
        return Book.objects.create(**validated_data)
    
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    

class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'type' ,'image', 'price', 'sale', 'quantity', 'des', 'category']

class UpdateBookSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['image', 'price', 'sale', 'quantity', 'des', 'category']

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.image = request.FILES.get('image')
        instance.price = validated_data.get('price')
        instance.sale = validated_data.get('sale')
        instance.quantity = validated_data.get('quantity')
        category_id = validated_data.pop('category')
        category_instance = Category.objects.filter(is_active__in=[True], id = category_id).first()
        if category_instance:
            instance.category = category_instance
        else:
            raise serializers.ValidationError('Category does not exist')
        
        instance.des = validated_data.get('des')
        instance.save()
        return instance
