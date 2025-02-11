from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customers
from .serializers import CustomersSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class CustomersSearchAPIView(APIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    def get(self, request):
        query = request.query_params.get('name', None)
        if query:
            users = Customers.objects.filter(name__icontains=query)
            serializer = CustomersSerializer(users, many=True)
            return Response(serializer.data)
        return Response({"error": "Vui lòng nhập từ khóa tìm kiếm!"}, status=400)
    
# class CustomersRegisterAPIView(APIView):
#     queryset = Customers.objects.all()
#     serializer_class = CustomersSerializer
#     def post(self, request):
#         serializer = CustomersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class CustomersLoginAPIView(APIView):
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsAuthenticated]

#     def get(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")

#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 "refresh": str(refresh),
#                 "access": str(refresh.access_token),
#                 "role": user.role  # Nếu User model có trường role
#             })
        
#         return Response({"error": "Thông tin đăng nhập không hợp lệ"}, status=status.HTTP_401_UNAUTHORIZED)