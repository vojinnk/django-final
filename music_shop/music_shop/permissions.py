from rest_framework.permissions import BasePermission


class SellerOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_seller


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
