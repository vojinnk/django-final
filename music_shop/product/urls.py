
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from product import views as product_views
from .views import ProductImageList, ProductImageDetail

router = DefaultRouter()

router.register(r'type', product_views.ProductTypeView)
router.register(r'', product_views.ProductView)


urlpatterns = [

    path('', include(router.urls)),
    

    path('productimages', ProductImageList.as_view(), name='productimages'),
    path('productimages/<int:pk>/', ProductImageDetail.as_view(), name='singleproductimage'),

   
   
]