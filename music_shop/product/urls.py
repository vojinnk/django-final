
from django.conf.urls import url
from django.urls import path, include
from product import views as product_views
from .views import ProductImageList, ProductImageDetail, ShippingList, ShippingDetail

urlpatterns = [

    path('', product_views.ProductView.as_view()),
    path('type', product_views.ProductType.as_view()),
    path('typeDetails/<int:id>/', product_views.ProductTypeDetails.as_view()),

    path('productimages', ProductImageList.as_view(), name='productimages'),
    path('productimages/<int:pk>/', ProductImageDetail.as_view(), name='singleproductimage'),

    path('shipping', ShippingList.as_view(), name='shipping'),
    path('shipping/<int:pk>/', ShippingDetail.as_view(), name='singleshipping'),
   
]