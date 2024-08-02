from django.db import models


# Create your models here.
class Hospitals(models.Model):
    name=models.CharField(primary_key=True,max_length=100)
    address=models.CharField(max_length=100,blank=True)
    phone=models.CharField(max_length=100,blank=True)
    email=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name
class Doctors(models.Model):
    name=models.CharField(max_length=100)
    doctor_id=models.CharField(primary_key=True,max_length=100)
    hospital=models.ForeignKey(Hospitals,on_delete=models.CASCADE)
    address=models.CharField(max_length=100,blank=True)
    phone=models.CharField(max_length=100,blank=True)
    email=models.CharField(max_length=100,blank=True)
    speciality=models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
    

class TestReport(models.Model):
    report_id = models.CharField(max_length=100)
    image = models.ImageField(upload_to='test_reports/')



class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    prescription_image = models.ImageField(upload_to='prescriptions/')