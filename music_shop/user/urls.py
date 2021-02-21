
from django.conf.urls import url
from user import views

urlpatterns = [
    url('signup', views.UserRegistration.as_view(), name='signup'),
    url('login', views.UserLogin.as_view(), name='login'),
    url('logout', views.UserLogout.as_view(), name='logout'),
    url('token', views.RefreshTokenUser.as_view(), name='refresh_token'),
    url('admin',views.UserGetAndDelete.as_view(), name = 'user_crud')
]