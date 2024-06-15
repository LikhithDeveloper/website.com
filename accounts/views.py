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


#@login_required(login_url='/staff_login/')

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
        fee = data.get('fee')
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        user_type = data.get('user_type')

        if password != confirm_password:
            messages.info(request, "Password missmatched")
            return redirect('/register/')

        else:
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
                queryset = Register.objects.get(username = username)
                if queryset.user_type == 'student':
                    Student_id.objects.create(
                    register1 = queryset,
                    course = course,
                    userid = username
                    )
                    Marks.objects.create(
                        register2 = queryset,
                    )
                    Fee.objects.create(
                        register3 = queryset,
                        fee = fee
                    )
                    Attendence.objects.create(
                        register4 = queryset,
                    )
                messages.info(request, "User created succesfully")
                return redirect('/register/')
            else:
                messages.info(request, "User is already exist")
                return redirect('/register/')



    return render(request,'register.html')



def student_login(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username = username)
        if not User.objects.filter(username=username):
            messages.error(request,'Invalid Username')
            return redirect('/student_login/')
        user = authenticate(username = username , password = password)
        if user:
            x = Register.objects.get(username = username)
            y = User.objects.get(username = username)
            if x.user_type == 'student':
                return redirect(f'/student/{username}')
            else:
                messages.error(request,'Only students can access to this portal')
                return redirect('/student_login/')
    return render(request,'login.html')

def staff_login(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username = username)
        if not User.objects.filter(username=username):
            messages.error(request,'Invalid Username')
            return redirect('/student_login/')
        user = authenticate(username = username , password = password)
        if user:
            x = Register.objects.get(username = username)
            y = User.objects.get(username = username)
            if x.user_type == 'teacher':
                return redirect('/details/')
            else:
                messages.error(request,'Only students can access to this portal')
                return redirect('/student_login/')
    return render(request,'login.html')


#@login_required(login_url='/staff_login/')
def details(request):
    queryset = Register.objects.filter(user_type = 'student')
    if request.GET.get('class_name'):
        queryset = queryset.filter(class_name__exact = request.GET.get('class_name')) #by using __exact we can get the records which exactly equal to the search
    if request.GET.get('id'):
        queryset = queryset.filter(username__icontains = request.GET.get('username')) # by using __icontains we can get the records which contains the search
    context = {'details':queryset}
    return render(request,'details.html',context)

def apply(request):
    return render(request,'apply.html')

def dashboard(request):
    return render(request,'dashboard.html')