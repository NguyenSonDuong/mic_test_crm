from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomersSearchAPIView, CustomersUpdateAPIView, CustomersReadAPIView, CustomersDeleteAPIView


urlpatterns = [
    path('search', CustomersSearchAPIView.as_view(), name='customers-search'),
    path('update', CustomersUpdateAPIView.as_view(), name='customers-update'),
    path('info', CustomersReadAPIView.as_view(), name='customers-read'),
    path('delete', CustomersDeleteAPIView.as_view(), name='customers-delete'),
]