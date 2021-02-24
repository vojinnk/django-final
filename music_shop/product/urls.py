
from django.conf.urls import url
from django.urls import path, include
from product import views as product_views

urlpatterns = [
    path('type', product_views.ProductType.as_view()),
    path('typeDetails/<int:id>/', product_views.ProductTypeDetails.as_view()),
   
]