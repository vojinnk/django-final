import jwt
from rest_framework import authentication,exceptions
from django.conf import settings
from user.models import User
from seller.models import Seller


class UserAuthentication(authentication.BaseAuthentication):
     def authenticate(self, request):
        request.user = None
        auth_data = authentication.get_authorization_header(request)

        if not auth_data :
            return None
        prefix,token = auth_data.decode('utf-8').split(' ')    
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY_USER_AT, algorithms=["HS256"])
            user = User.objects.get(pk=payload['id'])
            print(user)
            print('hej')
            return (user,token)
        except jwt.DecodeError as indetifier :
            raise exceptions.AuthenticationFailed('Your token is invalid')

        except jwt.ExpiredSignatureError as indetifier :
            raise exceptions.AuthenticationFailed('Your token is expired')


class SellerAuthentication(authentication.BaseAuthentication):
     def authenticate(self, request):
        request.user = None
        auth_data = authentication.get_authorization_header(request)

        if not auth_data :
            return None
        prefix,token = auth_data.decode('utf-8'). split(' ')    
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY_SELLER_AT, algorithms=["HS256"])
            user = Seller.objects.get(pk=payload['id'])
            return (user,token)
        except jwt.DecodeError as indetifier :
            raise exceptions.AuthenticationFailed('Your token is invalid')

        except jwt.ExpiredSignatureError as indetifier :
            raise exceptions.AuthenticationFailed('Your token is expired')


