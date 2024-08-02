from django.shortcuts import render, redirect
from .models import Hospitals,Doctors,Appointment
from django.contrib import messages
from .forms import AppointmentForm, TestReportForm, PrescriptionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def home(request):
    hospitals=Hospitals.objects.all()
    context={'hospitals':hospitals}
    return render(request, 'home.html',context)
def doctor(request):
    doctors=Doctors.objects.all()
    context={'doctors':doctors}
    return render(request, 'doctor.html',context)



def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment created successfully.')
            return redirect('appointments_list')
    else:
        form = AppointmentForm()
    return render(request, 'create_appointment.html', {'form': form})

def appointments_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments_list.html', {'appointments': appointments})

def add_report(request):
    if request.method == 'POST':
        form = TestReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TestReportForm()
    return render(request, 'add_report.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        
        x=User.objects.create_user(username=username,email=email,password=password)
        x.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'sign_up.html')



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            return render(request,'admin_user.html')
        else:
            messages.info(request,'Username OR password is incorrect')
    else:
        return render(request, 'login.html')
    
def prescription_view(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PrescriptionForm()
    return render(request, 'prescription.html', {'form': form})