from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone 

# Create your views here.
def attendence(request):
    queryset = Attendence.objects.all()
    
    if request.method == "POST":
        data = request.POST
        #print(data)
        for key in data:
            if key.startswith('studentId_'):
                index = key.split('_')[1]
                #print(index)
                studentId = data.get(f'studentId_{index}')
                attendance = data.get(f'attendance_{index}')
                # print(studentId)
                # print(attendance)
                try:
                    attendance_record = queryset.get(register4__username=studentId)
                    attendance_record.count += int(attendance)
                    attendance_record.save()

                    user = User.objects.get(username=studentId)
                    joined_date = user.date_joined
                    
                    today = timezone.localtime(timezone.now())
                    delta = today - joined_date  # Calculate timedelta
                    #print(abs(delta.days) +1)  # Print the difference in days
                    percentage = (attendance_record.count/(abs(delta.days) +1) ) * 100
                    attendance_record.percentage = percentage
                    attendance_record.save()

                except Attendence.DoesNotExist:
                    print(f"Attendance record for user '{studentId}' does not exist.")
                except User.DoesNotExist:
                    print(f"User with username '{studentId}' does not exist.")

                #print(today.strftime('%Y-%m-%d'))

                # Process each row's data here (e.g., save to database, update attendance, etc.)
                # Example: Updating attendance (assuming you have a suitable method on the model)
                # try:
                #     attendance_record = Attendence.objects.get(register4__username=studentId)
                #     attendance_record.count += 1 if attendance == '1' else 0
                #     attendance_record.save()
                # except Attendence.DoesNotExist:
                #     pass  # Handle the case where the student record does not exist

    if request.GET.get('search'):
        search_term = request.GET.get('search')
        queryset = queryset.filter(register4__class_name__exact=search_term)
    
    context = {'ids': queryset}
    return render(request, 'attendence.html', context)