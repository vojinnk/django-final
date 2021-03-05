from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,mixins,viewsets
from rest_framework import filters
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
    permission_classes = [AdminOnly]
    authentication_classes = [UserAuthentication]

class ProductView(mixins.ListModelMixin,
    mixins.RetrieveModelMixin,mixins.CreateModelMixin,
    mixins.UpdateModelMixin,mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    
    permission_classes = [UserOnly]
    authentication_classes = [UserAuthentication]
    queryset=Product.objects.all()
    search_fields = ["product_name","product_type__product_type"]
    filter_backends = (filters.SearchFilter,)

    def get_serializer_class(self):
        if self.request.method == "POST" or self.request.method == "PUT":
            return CUProductSerializer
        else:
            return ProductSerializer

    def create(self, request, *args, **kwargs):

        data = request.data
        data["seller"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset=Product.objects.all().order_by("-createdtime")
        maxPrice = self.request.query_params.get('maxPrice', None)
        minPrice = self.request.query_params.get('minPrice', None)
        if maxPrice is not None:
            queryset=queryset.filter(price__lte=maxPrice)
        if minPrice is not None:
            queryset=queryset.filter(price__gte=minPrice)
        return queryset


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
    
