from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import*

# Create your models here.


class Student_id(models.Model):
    register1 = models.OneToOneField(Register,on_delete=models.CASCADE)
    course = models.CharField(max_length=20)
    userid = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.register.first_name} of ID {self.id}'

class Marks(models.Model):
    register2 = models.ForeignKey(Register,on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.register1.username} got marks {self.marks}'

class Fee(models.Model):
    register3 = models.OneToOneField(Register,on_delete=models.CASCADE)
    fee = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.register2.username}'
    
class Attendence(models.Model):
    register4 = models.OneToOneField(Register,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)


