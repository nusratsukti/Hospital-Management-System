from django.contrib import admin
from .models import Hospitals,Doctors,Appointment,TestReport,Prescription
# Register your models here.
admin.site.register(Hospitals)
admin.site.register(Doctors)
admin.site.register(Appointment)
admin.site.register(TestReport)
admin.site.register(Prescription)
