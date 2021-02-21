from rest_framework import serializers
from .models import Seller,SellerToken
from django.contrib.auth import authenticate
import jwt 
from django.conf import settings

class SellerSerializer(serializers.ModelSerializer):
    sellerimages= serializers.StringRelatedField(many = True)
    class Meta:
        model = Seller
        fields = '[seller_id,name,email,number,packet,description,sellerimages]'



class SellerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    class Meta:
        model = Seller
        fields = '__all__'
 
    def create(self, validated_data):
        return Seller.objects.create_seller(**validated_data)
        


class SellerLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
    
        username = data.get('username', None)
        password = data.get('password', None)
        print (password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            raise serializers.ValidationError(
                'Seller with this email and password is not found.'
            )
        try:
            userObj = Seller.objects.get(email=user.email)

        except user.DoesNotExist:
            raise serializers.ValidationError(
                'Seller with given email and password does not exists'
            )   
 
        accesstoken = jwt.encode({
            'id': userObj.id,
            'exp': '20m'
        }, settings.JWT_SECRET_KEY_SELLER_AT, algorithm='HS256')
        refreshtoken = jwt.encode({
            'id': userObj.id
        }, settings.JWT_SECRET_KEY_SELLER_RT, algorithm='HS256')
        
      
        try:
            print(userObj.id)
            saverefresh = SellerToken.objects.create(seller_id=userObj.id,token= refreshtoken)
            saverefresh.save()

        except  Exception as e:
            raise serializers.ValidationError(
                'filed to save refreshtoken'
            )   

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
 
        return {
            'accesstoken': accesstoken,
            'refreshtoken':refreshtoken
        }


class SellerTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=128, write_only=True)
    def validate(self, data):
    
        try:
            token = SellerToken.objects.get(token=data.token)
            payload = jwt.decode(data.token, settings.JWT_SECRET_KEY_SELLER_RT, algorithms="HS256")
            accesstoken = jwt.encode({
            'id': token.seller,
            'exp':'20m'
        }, settings.JWT_SECRET_KEY_SELLER_AT, algorithm='HS256').decode('utf-8')
       
        except jwt.DecodeError as indetifier :
            raise exceptions.AuthenticationFailed('Your token is invalid')

        except jwt.ExpiredSignatureError as indetifier :
            raise exceptions.AuthenticationFailed('Your token is expired')
      
        return {
            'accesstoken': accesstoken
        }


class SellerLogOutSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
    
        try:
            payload = jwt.decode(data.token, settings.JWT_SECRET_KEY_SELLER_RT, algorithms="HS256")
            seller = Seller.objects.get(pk=payload['id']) #provjera da li postoji user
            SellerToken.objects.delete(token = data.token) #brise se refresh token
        except jwt.DecodeError as indetifier :
            raise exceptions.AuthenticationFailed('Your token is invalid')

        except jwt.ExpiredSignatureError as indetifier :
            raise exceptions.AuthenticationFailed('Your token is expired')    

        except  Exception as e:
            raise serializers.ValidationError(
                'filed to log out'
            )   
        return True

               