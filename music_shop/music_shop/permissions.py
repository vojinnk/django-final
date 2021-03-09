from rest_framework.permissions import BasePermission,SAFE_METHODS


class SellerOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_seller


class UserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS :
            return True
        elif request.user :
            return True
        else :
            return False
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            print("dozvola object")
            print(obj.seller)
            print(request.user)
            return obj.seller == request.user

class UserOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user :
            return True
        else :
            return False


class AllowAny(BasePermission):
    def has_permission(self,request,view) : 
        print(request)
        return True

class AdminOnly(BasePermission):
    def has_permission(self, request, view):
            if(request.user.is_superuser==True):
                return True
            else :
                return False
