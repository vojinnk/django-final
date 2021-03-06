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
    seller = UserSerializer()
    product_type= ProductTypeSerializer()
    images = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["id","product_name","price","shipping_time","seller","product_type","images"]
    def get_images(self, obj):
       images = Product_image.objects.all() # will return product query set associate with this category
       response = ProductImageSerializer(images, many=True).data
       return response
class CUProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude=[]
    


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_image
        fields = '__all__'



