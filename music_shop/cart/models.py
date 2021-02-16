from django.db import models
from product.models import Product
from user.models import User
# Create your models here.

class Cart(models.Model):
    user_id = models.OneToOneField(User, related_name='cart',on_delete=models.CASCADE)
    product_id= models.ManyToManyField(Product, related_name='cart', null=True ) #sam kreira cart_prduct
    order_time= models.TimeField(auto_now_add=True)   