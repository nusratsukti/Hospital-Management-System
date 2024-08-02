"""hospital_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor/', views.doctor, name='doctor'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('appointments_list/', views.appointments_list, name='appointments_list'),
    path('add_report/', views.add_report, name='add_report'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('prescription/', views.prescription_view, name='prescription'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)