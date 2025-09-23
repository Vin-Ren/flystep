from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(max_length=255)
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) # New product spotlight
    updated_at = models.DateTimeField(auto_now=True) # Kalo ada update, mungkin temporary featured?
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # Punya siapa 
