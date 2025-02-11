from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomersSearchAPIView


urlpatterns = [
    path('search', CustomersSearchAPIView.as_view(), name='customers-search'),
]