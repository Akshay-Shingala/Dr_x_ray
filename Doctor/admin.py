from django.contrib import admin
from .models import DoctorModel, PatientModel
# Register your models here.

class DoctorModelAdmin(admin.ModelAdmin):
    list_display = ['name','email','created_at']
    search_fields = ['name','email']
    list_filter = ['created_at']

class PatientModelAdmin(admin.ModelAdmin):
    list_display = ['name','age','created_at','disease','X_ray_image']
    search_fields = ['name','age']
    list_filter = ['created_at']

admin.site.register(DoctorModel,DoctorModelAdmin)
admin.site.register(PatientModel,PatientModelAdmin)
