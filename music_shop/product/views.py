from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from auth.backends import UserAuthentication
from music_shop.permissions import AdminOnly,UserOnly,AllowAny
from .models import Product_type,Product,Product_image

from music_shop.permissions import UserOnly,AllowAny,AdminOnly
from .serializers import ProductTypeSerializer

# Create your views here.
class ProductType(APIView):
    authentication_classes=[]
    permission_classes = (AllowAny,)
    serializer_class = ProductTypeSerializer

    def get(self,request):
        productTypes = Product_type.objects.all()
        serializer =self.serializer_class(productTypes,many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    
