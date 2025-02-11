from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customers
from .serializers import CustomersSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_core.drf_modules.user.permissions.customers_permissions import IsCustomer
from rest_framework.permissions import IsAuthenticated
from drf_core.drf_modules.user.serializers import UserSerializer

class CustomersSearchAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsCustomer]


    def get(self, request):
        query = request.query_params.get('name', None)
        if query:
            users = Customers.objects.filter(name__icontains=query)
            serializer = CustomersSerializer(users, many=True)
            return Response(serializer.data)
        return Response({"error": "Vui lòng nhập từ khóa tìm kiếm!"}, status=400)
    
class CustomersReadAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsCustomer]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user) 
        return Response(serializer.data)
    
class CustomersUpdateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsCustomer]

    def post(self, request):
        user = request.user 
        if not user:
            Response({"error": "Vui lòng đăng nhập"}, status=400)
        serializer = CustomersSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"success": "Cập nhật thông tin thành công"}, status=200)

class CustomersDeleteAPIView(APIView):    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsCustomer]

    def delete(self, request):
        user = request.user 
        if not user:
            Response({"error": "Vui lòng đăng nhập"}, status=400)
        user.delete()
        return Response({"success": "Đã xóa thành công"}, status=200)