from django.db import models
from user.models import User
from product.models import Product


class Order(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE) 
    product_id= models.ManyToManyField(Product) 
    order_time= models.TimeField(auto_now_add=True)   
