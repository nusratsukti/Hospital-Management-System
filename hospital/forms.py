from django import forms
from .models import Appointment, TestReport, Prescription

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('name', 'email', 'date', 'time')
        





class TestReportForm(forms.ModelForm):
    class Meta:
        model = TestReport
        fields = ['report_id', 'image']

# class User_form(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['name','email','password']
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['doctor_id', 'prescription_image']