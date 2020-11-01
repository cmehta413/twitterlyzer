from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
 
 
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)

