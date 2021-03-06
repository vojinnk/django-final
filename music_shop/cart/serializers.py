from rest_framework import serializers, exceptions
from .models import Cart
from seller.models import Seller
from product.serializers import ProductSerializer



class CartSerializer(serializers.ModelSerializer):
    product= ProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['product']
    def update(self,validated_data,instance):
        products = validated_data.pop('products')
        cart = instance
        for product in products: 
            cart.product.add(product)