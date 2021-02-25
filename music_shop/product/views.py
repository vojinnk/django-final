from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from auth.backends import UserAuthentication
from music_shop.permissions import AdminOnly,UserOnly,AllowAny
from .models import Product_type,Product,Product_image

from music_shop.permissions import UserOnly,AllowAny,AdminOnly
from .serializers import ProductTypeSerializer, ProductSerializer

# Create your views here.
class ProductType(APIView):
    authentication_classes=[]
    permission_classes = (AllowAny,)
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
    authentication_classes=[]
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

class ProductView(APIView):
    authentication_classes=[]
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    def get(self,request):
        products = Product.objects.all()
        serializer = self.serializer_class(products,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)