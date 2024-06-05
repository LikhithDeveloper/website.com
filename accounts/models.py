from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Register(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField(default='email')
    address = models.TextField()
    class_name = models.CharField(max_length=10,default='admin')
    course = models.CharField(max_length=10 , default='admin')
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10)
    user_type = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'{self.username}'
    

