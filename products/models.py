from django.contrib.auth.models import User
from django.db import models

class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    sold = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)