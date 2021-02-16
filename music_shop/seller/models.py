from django.db import models
from user.models import User 
from  django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager


class SellerManager(BaseUserManager):
 
    def create_seller(self,email, number, description, packet, password,username=None,is_seller =True):
        if email is None:
            raise TypeError('Seller must have an email address.')
        seller = Seller(description=description,username=username,
                        email=self.normalize_email(email),
                        number=number, packet=packet)
        seller.set_password(password)
        seller.save()
        return seller


class Seller(User):
    packet = models.IntegerField(default=1)
    description = models.CharField(max_length=200, blank=False,null=False )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'description', 'password','packet']
    readonly_fields=('is_seller', )
    objects = SellerManager()
 
 
    def __str__(self):
        return self.name

class SellerToken(models.Model):
    token= models.CharField(max_length=200,null=True,db_index=True) 
    seller= models.ForeignKey(Seller, related_name='seller_token',on_delete=models.CASCADE)
    def __str__(self):
        return self.token
       