from rest_framework import serializers,exceptions
import datetime
from .models import User,UserToken
from django.conf import settings
from django.contrib.auth import authenticate
import jwt 

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = '__all__'
 
    def create(self, validated_data):
        if("is_superuser" in validated_data) :
             return User.objects.create_superuser(**validated_data)
        else :
            return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=300, write_only=True)

    def validate(self, data):
    
        username = data.get('username', None)
        password = data.get('password', None)
 
        user = authenticate(username=username, password=password)
 
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password is not found.'
            )
        try:
            userObj = User.objects.get(username=user.username)

        except User.DoesNotExist:
            raise serializers.ValidationError(
                'A user with given username and password does not exists'
            )
        accesstoken = jwt.encode({
            'id': userObj.id,
            'role': userObj.is_superuser,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=20)
        }, settings.JWT_SECRET_KEY_USER_AT, algorithm='HS256')
        refreshtoken = jwt.encode({
            'id': userObj.id,
            'role': userObj.is_superuser,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }, settings.JWT_SECRET_KEY_USER_RT, algorithm='HS256')
      
        try:
            saverefresh = UserToken.objects.create(user_id=userObj.id,token=refreshtoken)
            saverefresh.save()
        except Exception as e:
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


class UserTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=300, write_only=True)

    def validate(self, data):
    
        try:
            token = data.get('token')
            print(token)
            tokenobj = UserToken.objects.get(token=token)
            print(tokenobj)
            payload = jwt.decode(tokenobj.token, settings.JWT_SECRET_KEY_USER_RT, algorithms=["HS256"])
            print(payload)
            accesstoken = jwt.encode({
            'id': payload["id"],
            'role': payload["role"],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, settings.JWT_SECRET_KEY_USER_AT, algorithm='HS256')
        except jwt.DecodeError as indetifier :
            print('je')
            raise exceptions.AuthenticationFailed('Your token is invalid')

        except jwt.ExpiredSignatureError as indetifier :
            print('jee')
            raise exceptions.AuthenticationFailed('Your token is expired')
        print(accesstoken)
        return {
            'accesstoken': accesstoken
        }


class UserLogOutSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=300, write_only=True)

    def validate(self, data):
    
        try:
            token = data.get('token')
            payload = jwt.decode(token, settings.JWT_SECRET_KEY_USER_RT, algorithms="HS256")
            user = User.objects.get(pk=payload['id']) #provjera da li postoji user
           # if user!=authuser :
            #   raise exceptions.AuthenticationFailed('Error, invalid token')

            UserToken.objects.get(token = token).delete() #brise se refresh token
        except jwt.DecodeError as indetifier :
            raise exceptions.AuthenticationFailed('Your token is invalid')

        except jwt.ExpiredSignatureError as indetifier :
            raise exceptions.AuthenticationFailed('Your token is expired')    

        except  Exception as e:
            raise serializers.ValidationError(
                'filed to log out'
            )   
        return True


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'number',
            'username',
            'email',
            "is_seller",
            "is_superuser"
        )
 