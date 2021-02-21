from rest_framework import status
from django.contrib.auth import authenticate
from user.models import User,UserToken
from user.serializers import UserLoginSerializer,UserSerializer, UserRegistrationSerializer,UserTokenSerializer,UserLogOutSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from music_shop.permissions import UserOnly,AllowAny,AdminOnly
from auth.backends import UserAuthentication
from cart.models import Cart


class UserLogin(APIView):
    authentication_classes=[]
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class UserLogout(APIView):
    authentication_classes = [UserAuthentication]
    permission_classes = (AllowAny,)
    serializer_class = UserLogOutSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RefreshTokenUser(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    def post(self, request):
        try:
            serializer = UserTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
 
class UserRegistration(APIView):
    permission_classes = (AllowAny,)
    authentication_classes=[]
    serializer_class = UserRegistrationSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user.id)
        try:
            Cart.objects.create(user_id=user.id)
        except Exception as e:
            print(e)
            return Response({ 'message': "Failed to create cart."},
                            status=status.HTTP_400_BAD_REQUEST)         
        return Response(serializer.data, status=status.HTTP_201_CREATED) 


class UserGetAndDelete(APIView):
    authentication_classes=[UserAuthentication]
    permission_classes = (AdminOnly,)
    def put(self,request):
        print(request.data["id"])
        try:
            user= User.objects.get(id=request.data["id"])
            token = UserToken.objects.filter(user=user)
            token.delete()
            return Response({True},status = status.HTTP_200_OK)
            
        except user.DoesNotExist as e: 
            return Response({"data":"user ne postoji"},status = status.HTTP_404_NOT_FOUND) 
         
       # try:
        #    token = UserToken.objects.filter(user=user, many=True)
         #   token.delete()
          #  return Response(status=status.HTTP_200_OK)      
        #except :
         #   print (e)
          #  return Response({"data":"user nije ulogovan"},status=status.HTTP_404_NOT_FOUND)     
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    def delete(self,request):
        try: 
            user = User.objects.get(id=request.data["id"]).delete()
            return Response(status=200)
        except User.DoesNotExist as e : 
            return Response({"data":"Korisnik nije pronadjen"},status= status.HTTP_404_NOT_FOUND)


