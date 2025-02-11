from drf_core.model_base.base_model import BaseModel
from django.db import models
from drf_core.models import User

class Customers(BaseModel):

    name = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField()


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer", null=True)

    def __str__(self):
        return self.name