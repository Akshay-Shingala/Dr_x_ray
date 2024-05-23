from django.db import models

# Create your models here.
# from django.db import models


class DoctorModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PatientModel(models.Model):
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    disease = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    X_ray_image = models.ImageField(upload_to='X_ray_images',blank=True,null=True)
    