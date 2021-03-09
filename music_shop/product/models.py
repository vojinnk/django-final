from django.db import models
from seller.models import Seller
 
class Product_type(models.Model):  #vrsta proizvoda (violina, gitara...)
    product_type = models.CharField(max_length=30, unique=True, blank=False ) 
 
    def __str__(self):
        return self.product_type


class Product(models.Model):
    seller = models.ForeignKey(Seller, related_name='products',on_delete=models.CASCADE)
    product_type = models.ForeignKey(Product_type, related_name='products',on_delete=models.CASCADE)
    product_name= models.CharField(max_length=30, unique=True, blank=False )
    price= models.FloatField(null=True)
    shipping_time=models.IntegerField(null=True)
    createdtime= models.TimeField(auto_now_add=True)   
 
    def __str__(self):
        return self.product_name


class Product_image(models.Model): #zbog veceg broja slika za jedan proizvod bolje da ova tabela bude posebna
    imageurl= models.CharField(max_length=200, unique=True, blank=False,null=False ) 
    product = models.ForeignKey(Product,related_name='productimages',on_delete=models.CASCADE)
 
    def __str__(self):
        return self.imageurl       