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
    address = models.TextField(null=True)
    class_name = models.CharField(max_length=10,default='admin')
    course = models.CharField(max_length=10 , default='admin')
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    user_type = models.CharField(max_length=10, choices=[
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ])
    #date_of_join = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.username} of course {self.course}'
    


# Signal to create user when ever user register

@receiver(post_save, sender=Register)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create(
            first_name=instance.first_name,
            last_name=instance.last_name,
            username=instance.username,
            email=instance.email,
            is_active=True,
        )
        user.set_password(instance.password)
        
        if instance.user_type == 'student':
            user.is_staff = False
            user.is_superuser = False
        elif instance.user_type == 'teacher':
            user.is_staff = True
            user.is_superuser = False
        elif instance.user_type == 'admin':
            user.is_staff = False
            user.is_superuser = True
        
        user.save()
