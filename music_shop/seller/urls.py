
from django.conf.urls import url
from seller import views

urlpatterns = [
    url('signup', views.SellerRegistration.as_view(), name='signup'),
    url('login', views.SellerLoginView.as_view(), name='login'),
    url('logout', views.SellerLogout .as_view(), name='logout'),
    url('token', views.RefreshTokenSeller.as_view(), name='refresh_token'),
]