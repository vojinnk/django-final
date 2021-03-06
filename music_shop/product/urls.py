
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from product import views as product_views


router = DefaultRouter()

router.register(r'type', product_views.ProductTypeView)
router.register(r'', product_views.ProductView)



urlpatterns = [

    path('', include(router.urls)),
    
   
   
]