from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')