from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from seller.serializers import SellerSerializer,SellerTokenSerializer,SellerLoginSerializer,SellerRegistrationSerializer,SellerLogOutSerializer
from seller.models import Seller,SellerToken
from music_shop.permissions import SellerOnly,AllowAny
from auth.backends import SellerAuthentication
from django.conf import settings
from django.contrib import auth
import jwt 


class SellerLoginView(APIView):
    authentication_classes= []
    permission_classes = (AllowAny,)
    serializer_class = SellerLoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class SellerLogout(APIView):
    authentication_classes = [SellerAuthentication]
    permission_classes = [SellerOnly]
    serializer_class = SellerLogOutSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RefreshTokenSeller(APIView):
    authentication_classes= []
    permission_classes = (AllowAny,)
    def post(self, request):
        try:
            token =  SellerToken.objects.get(token=request.data.token)
            serializer = SellerTokenSerializer(data=token)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data)
        except Exception as e:
            return Response({'data': None, 'message': "Failed to products.",
                             'success': False},
                            status=status.HTTP_400_BAD_REQUEST)    


class SellerRegistration(APIView):
    permission_classes = (AllowAny,)
    authentication_classes=[]
    serializer_class = SellerRegistrationSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)                            