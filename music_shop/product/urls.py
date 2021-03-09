
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from product import views as product_views


router = DefaultRouter()

router.register(r'type', product_views.ProductTypeView)
router.register(r'', product_views.ProductView)
router.register(r'images/', product_views.ImagesView)


urlpatterns = [

    path('', include(router.urls)),
    path('productimages', product_views.ProductImageList.as_view(), name='productimages'),
    path('productimages/<int:pk>/', product_views.ProductImageDetail.as_view(), name='singleproductimage'),
    
   
   
]