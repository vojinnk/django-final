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
from .models import Product_type,Product,Product_image, Shipping_detail
from music_shop.permissions import UserOnly,AllowAny,AdminOnly

from .serializers import ProductTypeSerializer, ProductSerializer, GetProductSerializer,ProductImageSerializer, ShippingDetailSerializer




# Create your views here.

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
    
