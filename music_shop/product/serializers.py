from rest_framework import serializers,exceptions
from .models import Product_type,Product,Product_image,Shipping_detail,Seller


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_type
        fields = '__all__'
    def create(self,validated_data):
        return Product_type.objects.create(**validated_data)
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields="__all__"