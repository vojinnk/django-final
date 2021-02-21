from django.db import models
from user.models import User 
from  django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager


class SellerManager(BaseUserManager):
 
    def create_seller(self,email, number, username,password,is_seller =True):
        if email is None:
            raise TypeError('Seller must have an email address.')
        seller = Seller(username=username,
                        email=self.normalize_email(email),
                        number=number, is_seller = True)
        seller.set_password(password)
        seller.save()
        return seller


class Seller(User):
    USERNAME_FIELD = 'username'
    readonly_fields=('is_seller', )
    objects = SellerManager()
 
    def __str__(self):
        return self.username

class SellerToken(models.Model):
    token= models.CharField(max_length=200,null=True,db_index=True) 
    seller= models.ForeignKey(Seller, related_name='seller_token',on_delete=models.CASCADE)
    def __str__(self):
        return self.token
       