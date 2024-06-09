"""
URL configuration for tdr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from students.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name = 'home'),
    path('register/',register,name = 'register'),
    path('student_login/',student_login,name='student_login'),
    path('details/',details,name='details'),
    path('apply/',apply,name='apply'),
    path('dashboard/',dashboard,name='dashboard'),
    path('staff_login/',staff_login,name='staff_login'),
    path('attendence/',attendence,name='attendence'),
    path('staff/<username>/',staff,name='staff')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
