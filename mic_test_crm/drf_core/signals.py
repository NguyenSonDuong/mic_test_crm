from django.db.models.signals import post_save
from django.dispatch import receiver
from drf_core.models import User
from .drf_modules.customers.models import Customers

# Khi một User mới được tạo, tạo Customer tương ứng
@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customers.objects.create(user=instance)

# Khi User được lưu, lưu luôn Customer
@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    instance.customer.save()