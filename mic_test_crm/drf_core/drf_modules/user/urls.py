from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomerRegisterAPIView, EmployeeRegisterAPIView, AdminRegisterAPIView, UserLoginAPIView


urlpatterns = [
    path('register/customer', CustomerRegisterAPIView.as_view(), name='customers_register'),
    path('register/employee', EmployeeRegisterAPIView.as_view(), name='employee_register'),
    path('register/admin', AdminRegisterAPIView.as_view(), name='admin_register'),
    path('login', UserLoginAPIView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]