from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from auth.backends import UserAuthentication,SellerAuthentication
from music_shop.permissions import AdminOnly,UserOnly,AllowAny
from seller.models import Seller
from seller.serializers import SellerSerializer
from user.models import User
from .models import Product_type,Product,Product_image

from music_shop.permissions import UserOnly,AllowAny,AdminOnly
from .serializers import ProductTypeSerializer, ProductSerializer,GetProductSerializer
# Create your views here.

class ProductView(generics.ListCreateAPIView):
    
    queryset=Product.objects.all()
    permission_classes=[AllowAny]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductSerializer
        else:
            return GetProductSerializer

class ProductType(APIView):
    authentication_classes=[UserAuthentication]
    permission_classes = (AdminOnly,)
    serializer_class = ProductTypeSerializer

    def get(self,request):
        productTypes = Product_type.objects.all()
        serializer =self.serializer_class(productTypes,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

class ProductTypeDetails(APIView):
    authentication_classes=[UserAuthentication]
    permission_classes = (AllowAny,)
    serializer_class = ProductTypeSerializer
    def get_object(self,id):
        try:
            return Product_type.objects.get(id=id)
        except Product_type.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        productType = self.get_object(id)
        serializer = self.serializer_class(productType)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        productType = self.get_object(id)
        print(productType)
        productType.delete()

        return Response(status=200)
'''
class ProductView(APIView):
    authentication_classes=[SellerAuthentication]
    permission_classes = (UserOnly,)
    serializer_class = ProductSerializer
    def get(self,request):
        products = Product.objects.all()
        serializer = self.serializer_class(products,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
      #  seller = Seller.objects.get(id=data["seller"])
        data['seller']=Seller.objects.get(id=data["seller"]).__dict__
        data['product_type']=Product_type.objects.get(id=data['product_type']).__dict__
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
'''