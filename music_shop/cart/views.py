from django.shortcuts import render
from .models import Product
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from auth.backends import UserAuthentication, SellerAuthentication

from music_shop.permissions import AdminOnly, UserOnly, AllowAny
from user.models import User
from .models import Cart
from music_shop.permissions import  UserOnly, AllowAny, AdminOnly

from .serializers import CartSerializer


class CartView(APIView):
    authentication_classes=[UserAuthentication]
    permission_classes = (AllowAny,)
    serializer_class = CartSerializer
    def put(self, request):
        cart = Cart.objects.get(user_id=request.user.id)
        products = request.data["products"]
        
        for product in products:
            cart.product.add(Product.objects.get(id=product))
        cart.save()
        serializer = self.serializer_class
        
        return Response({"DONE"},status=status.HTTP_201_CREATED)
        #serializer = self.serializer_class(data=pr,instance = cart)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        #return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def get(self, request):
        
        cart = Cart.objects.get(user_id=request.user.id)
        serializer = self.serializer_class(cart)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)


    def delete(self,request):
        try:    
            cart = Cart.objects.get(user_id = request.user.id).delete()
            return Response(status=200)
        except Cart.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)   
