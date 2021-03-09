from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,mixins,viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from auth.backends import UserAuthentication,SellerAuthentication
from django.core.files.storage import FileSystemStorage
import os

from music_shop.permissions import AdminOnly,UserOnly,AllowAny,UserOrReadOnly
from seller.models import Seller
from seller.serializers import SellerSerializer
from user.models import User
from .models import Product_type,Product,Product_image
from music_shop.permissions import UserOnly,AllowAny,AdminOnly

from .serializers import ProductImageSerializer, ProductTypeSerializer, ProductSerializer,CUProductSerializer




# Create your views here.

class ProductTypeView(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset=Product_type.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [AdminOnly]
    authentication_classes = [UserAuthentication]
    def get_permissions(self):
        if (self.action in ['retrieve','list']):
            retrieve_permission_list = [AllowAny]
            return [permission() for permission in retrieve_permission_list]
        else:
            return super().get_permissions()

class ProductView(mixins.ListModelMixin,
    mixins.RetrieveModelMixin,mixins.CreateModelMixin,
    mixins.UpdateModelMixin,mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    
    permission_classes = [UserOrReadOnly ]
    authentication_classes = [SellerAuthentication]
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ["product_name","product_type__product_type"]
    filter_backends = (filters.SearchFilter,)
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method == "POST" or self.request.method == "PUT":
            return CUProductSerializer
        else:
            return ProductSerializer
    
    def get_permissions(self):
        if self.action in ['retrieve','list']:
            retrieve_permission_list = [AllowAny]
            return [permission() for permission in retrieve_permission_list]
        else:
            return super().get_permissions()

    def create(self, request, *args, **kwargs):
        data = request.POST.copy()
        fs = FileSystemStorage()

        data["seller"] = request.user.id
        images = request.FILES.getlist("pictures")
        imageserializer=ProductImageSerializer
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print(serializer.validated_data)
        for f in images:
            file = fs.save(f.name, f)
            #print(os.path.abspath("MEDIA/"+file))
            imgdata={}
            imgdata['imageurl']=os.path.abspath("MEDIA/"+file)
            imgdata['product']=Product.objects.get(product_name=serializer.validated_data['product_name']).id
            img = imageserializer(data=imgdata)
            img.is_valid(raise_exception=True)
            img.save() 
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset=Product.objects.all().order_by("-createdtime")
        maxPrice = self.request.query_params.get('maxPrice', None)
        minPrice = self.request.query_params.get('minPrice', None)
        product_type = self.request.query_params.get('product_type', None)
        if maxPrice is not None:
            queryset=queryset.filter(price__lte=maxPrice)
        if minPrice is not None:
            queryset=queryset.filter(price__gte=minPrice)
        if product_type is not None:
            queryset=queryset.filter(product_type=product_type)
        return queryset
    


class ImagesView(mixins.ListModelMixin,
    mixins.RetrieveModelMixin,mixins.CreateModelMixin,
    mixins.UpdateModelMixin,mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    authentication_classes = []
    queryset = Product_image.objects.all()
    serializer_class = ProductImageSerializer

class ProductImageList(generics.ListCreateAPIView):
    queryset = Product_image.objects.all()
    serializer_class = ProductImageSerializer


class ProductImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product_image.objects.all()
    serializer_class = ProductImageSerializer