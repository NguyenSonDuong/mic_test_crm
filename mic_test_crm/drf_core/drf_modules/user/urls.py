from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomersRegisterAPIView, CustomersSearchAPIView,CustomersLoginAPIView


urlpatterns = [
    path('search', CustomersSearchAPIView.as_view(), name='customers-search'),
    path('register', CustomersRegisterAPIView.as_view(), name='customers-register'),
    path('login', CustomersLoginAPIView.as_view(), name='customers_login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]