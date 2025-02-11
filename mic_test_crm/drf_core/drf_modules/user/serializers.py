from drf_core.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from drf_core.drf_modules.customers.serializers import CustomersSerializer

class UserSerializer(serializers.ModelSerializer):
    info = CustomersSerializer(source="customer")
    # employee = EmployeeSerializer()
    class Meta:
        model = User
        fields = ['uuid', "username", "email", "info", 'role']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'required': True, 'read_only': False} ,
            'username': {'required': True} ,
            }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        # Kiểm tra xem email và password có hợp lệ không
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        refresh = RefreshToken.for_user(user)

        return {
            "email": user.email,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }