from django.conf.urls import url
from django.urls import path, include
from .import views as cart_views

urlpatterns = [
    path('', cart_views.CartView.as_view()),
]