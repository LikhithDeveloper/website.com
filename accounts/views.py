from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from students.models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        mobile_number = data.get('mobile_number')
        email = data.get('email')
        address = data.get('address')
        class_name = data.get('class_name')
        course = data.get('course')
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        user_type = data.get('user_type')

        x = Register.objects.filter(username = username)
        if not x.exists():
            Register.objects.create(
            first_name = first_name,
            last_name = last_name,
            mobile_number = mobile_number,
            email = email,
            address = address,
            class_name = class_name,
            course = course,
            username = username,
            password = password,
            user_type = user_type
            )
            messages.info(request, "User created succesfully")
            return redirect('/register/')
        else:
            messages.info(request, "User is already exist")
            return redirect('/register/')



    return render(request,'register.html')