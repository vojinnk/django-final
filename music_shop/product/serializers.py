from rest_framework import serializers,exceptions
from seller.models import Seller
from .models import Product_type,Product,Product_image
from user.serializers import UserSerializer
from seller.serializers import SellerSerializer


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_type
        exclude=[]
    

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_image
        exclude=[]

class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    product_type= ProductTypeSerializer()
    productimages = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = ["id","product_name","price","shipping_time","seller","product_type","productimages"]
    

class CUProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude=[]
    





