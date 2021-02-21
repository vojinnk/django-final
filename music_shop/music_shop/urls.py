
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views


urlpatterns = [
    url(r'^user/', include('user.urls')),
    #url(r'^product/', include('products.urls')),
    #url(r'^orders/', include('orders.urls')),
    url(r'^seller/', include('seller.urls')),
    #url(r'^cart/', include('cart.urls')),
    #path('admin/', admin.site.urls),
]