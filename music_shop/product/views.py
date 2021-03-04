from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,mixins,viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from auth.backends import UserAuthentication,SellerAuthentication

from music_shop.permissions import AdminOnly,UserOnly,AllowAny
from seller.models import Seller
from seller.serializers import SellerSerializer
from user.models import User
from .models import Product_type,Product,Product_image, Shipping_detail
from music_shop.permissions import UserOnly,AllowAny,AdminOnly

from .serializers import ProductImageSerializer, ShippingDetailSerializer, ProductTypeSerializer, ProductSerializer,CUProductSerializer




# Create your views here.

class ProductTypeView(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset=Product_type.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

class ProductView(mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):
    
    permission_classes = [AllowAny]
    authentication_classes = []
    queryset=Product.objects.all()
    
    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return CUProductSerializer
        else:
            return ProductSerializer




class ProductImageList(generics.ListCreateAPIView):
    queryset = Product_image.objects.all()
    serializer_class = ProductImageSerializer


class ProductImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product_image.objects.all()
    serializer_class = ProductImageSerializer

class ShippingList(generics.ListCreateAPIView):
    queryset = Shipping_detail.objects.all()
    serializer_class = ShippingDetailSerializer


class ShippingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipping_detail.objects.all()
    serializer_class = ShippingDetailSerializer
    
