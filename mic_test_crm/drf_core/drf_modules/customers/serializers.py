from .models import Customers
from rest_framework import serializers
import datetime
import re
class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['name', "birth_date",'phone', 'address']

    def validate_name(self, value):
        """ Kiểm tra tên không có số & ký tự đặc biệt """
        pattern = r'^[A-Za-zÀ-ỹ\s]+$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Tên chỉ được chứa chữ cái và khoảng trắng.")
        return value

    def validate_phone(self, value):
        """ Kiểm tra số điện thoại có đúng định dạng không """
        if not value.isdigit():
            raise serializers.ValidationError("Số điện thoại phải là số.")
        if len(value) == 10:
            raise serializers.ValidationError("Số điện thoại phải có 10 số.")
        return value
    
    def validate_dob(self, value):
        """ Kiểm tra ngày sinh hợp lệ """
        today = datetime.today().date()
        
        if value > today:
            raise serializers.ValidationError("Ngày sinh không thể lớn hơn ngày hiện tại.")
        
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 18:
            raise serializers.ValidationError("Khách hàng phải trên 18 tuổi.")
        
        return value
    
    def create(self, validated_data):
        return Customers.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """Hàm cập nhật thông tin User"""
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.save()
        return instance