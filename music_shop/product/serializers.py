from rest_framework import serializers,exceptions
from seller.models import Seller
from .models import Product_type,Product,Product_image
from user.serializers import UserSerializer
from seller.serializers import SellerSerializer


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_type
        exclude=[]
    
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        depth=1
        exclude=[]
        
class CUProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude=[]
    


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_image
        fields = '__all__'



