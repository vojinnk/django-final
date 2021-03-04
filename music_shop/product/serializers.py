from rest_framework import serializers,exceptions
from seller.models import Seller
from .models import Product_type,Product,Product_image,Shipping_detail
from user.serializers import UserSerializer
from seller.serializers import SellerSerializer


class ProductTypeSerializer(serializers.ModelSerializer):
   # product = serializers.PrimaryKeyRelatedField(many=True,queryset=Product.objects.all())
    class Meta:
        model = Product_type
        fields = '__all__'
    
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class GetProductSerializer(serializers.ModelSerializer):
    product_type=ProductTypeSerializer()
    seller = UserSerializer()
    class Meta:
        model = Product
        fields = "__all__"

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_image
        fields = '__all__'

class ShippingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_detail
        fields = '__all__'


