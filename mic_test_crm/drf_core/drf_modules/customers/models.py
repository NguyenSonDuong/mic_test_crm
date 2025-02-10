from drf_core.model_base.base_model import BaseModel
from django.db import models

class Customers(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name