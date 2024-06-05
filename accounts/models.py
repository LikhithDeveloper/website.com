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
        return f'{self.username} of course {self.course}'
    

@receiver(post_save, sender=Register)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'student':
            User.objects.create(
            first_name = instance.first_name,
            last_name  = instance.last_name,
            username = instance.username,
            password = instance.password,
            email = instance.email,
            is_active = True,
            is_staff = False,
            is_superuser = False
        )
        elif instance.user_type == 'teacher':
            User.objects.create(
            first_name = instance.first_name,
            last_name  = instance.last_name,
            username = instance.username,
            password = instance.password,
            email = instance.email,
            is_active = True,
            is_staff = True,
            is_superuser = False
        )
        elif instance.user_type == 'admin':
            User.objects.create(
            first_name = instance.first_name,
            last_name  = instance.last_name,
            username = instance.username,
            password = instance.password,
            email = instance.email,
            is_active = True,
            is_staff = False,
            is_superuser = True
        )
    else:
        instance.profile.save()

