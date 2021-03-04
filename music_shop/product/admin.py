from django.contrib import admin
from .models import Product_type, Product, Shipping_detail, Product_image
# Register your models here.


admin.site.register(Product_type)
admin.site.register(Product)
admin.site.register(Shipping_detail)
admin.site.register(Product_image)