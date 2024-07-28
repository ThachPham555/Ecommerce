from rest_framework import serializers
from .models import Brand, Mobile

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id' ,'name', 'des']
        
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class MobileSerializer(serializers.ModelSerializer):
    brand_id = serializers.CharField(write_only=True)

    class Meta:
        model = Mobile
        fields = ['id', 'title', 'publisher', 'image', 'price', 'sale', 'quantity', 'des', 'brand']
    
    def create(self, validated_data):
        brand = validated_data.pop('brand', None)
        image = validated_data.pop('image', None)
        request = self.context.get('request')

        if brand:
            brand_instance = Brand.objects.filter(is_active__in=[True], id=brand).first()
            if brand_instance:
                validated_data['brand'] = brand_instance
            else:
                raise serializers.ValidationError('Brand does not exits')
        return Mobile.objects.create(image=request.FILES.get('image'), **validated_data)
    
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    

class MobileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ['id', 'title', 'publisher', 'type', 'image', 'price', 'sale', 'quantity', 'des', 'brand']

class UpdateMobileSerializer(serializers.ModelSerializer):
    brand_id = serializers.CharField(write_only=True)

    class Meta:
        model = Mobile
        fields = ['image', 'price', 'sale', 'quantity', 'des', 'brand']

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.image = request.FILES.get('image')
        instance.price = validated_data.get('price')
        instance.sale = validated_data.get('sale')
        instance.quantity = validated_data.get('quantity')
        brand_id = validated_data.pop('brand')
        brand_instance = Brand.objects.filter(is_active__in=[True], id = brand_id).first()
        if brand_instance:
            instance.brand = brand_instance
        else:
            raise serializers.ValidationError('Brand does not exist')
        
        instance.des = validated_data.get('des')
        instance.save()
        return instance
