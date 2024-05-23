from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import DoctorModel, PatientModel
from django.contrib.auth.hashers import make_password , check_password
from django.core.files.storage import FileSystemStorage
from .utils import model_predict
import os
import io

def login(request):
    if request.session.get('doctor_id'):
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = DoctorModel.objects.filter(email=username).first()
        if user:
            if check_password(password, user.password):
                request.session['doctor_id'] = user.id
                request.session['doctor_email'] = user.email
                messages.success(request, 'Logged in successfully')
                return redirect('index')
            else:
                messages.error(request, 'Invalid credentials')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def register(request):
    if request.session.get('doctor_id'):
        return redirect('index')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        DoctorModel.objects.create(name=name, email=email, password=make_password(password))
        messages.success(request, 'Account created successfully')
        return redirect('login')
    return render(request, 'register.html')


from .vectordb import *
from .embed_gen import *
def check_valid_image(img):
    # image = "images/burger_crop.jpg"
    # save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), img)
    result = search_image(img_embed=get_image_embedding_vgg16_test(img)[0], collection_name="x_ray_images")
    print("Result: ", result)
    for i in result:
        print("id: ", i.id, "payload: ", i.payload, "score: ", i.score)
    return result

def index(request):
    if not request.session.get('doctor_id'):
        return redirect('login')
    if request.method == 'POST':
        save_path = ""
        try:
            name = request.POST.get('name')
            age = request.POST.get('age')
            X_ray_image = request.FILES.get('X_ray_image')

            print("images::::",type(X_ray_image))
            save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), X_ray_image.name)
            with open(save_path, 'wb+') as destination:
                for chunk in X_ray_image.chunks():
                    destination.write(chunk)

            # print("Saved X_ray_image", fs.url(filename))
            score = check_valid_image(save_path)
            if score[-1].score < 1200:
                os.remove(save_path)
                messages.warning(request, 'Please Enter valid X-ray Image!')
                return redirect('index')
            
            disease = model_predict(X_ray_image.name)
            doctor = DoctorModel.objects.get(id=request.session['doctor_id'])
            print("disease: ", doctor.name)
            patient = PatientModel.objects.create(doctor = doctor, name=name, age=age, disease=disease , X_ray_image=X_ray_image)
            os.remove(save_path)
            messages.success(request, 'Patient added successfully')
            return redirect('report',id=patient.id)
        except Exception as e:
            print(e)
            os.remove(save_path)
            messages.warning(request, 'Some error accuring during image process, Please try with another image!')
            return redirect('index')
    
    patients = PatientModel.objects.filter(doctor__id = request.session['doctor_id']).order_by('-created_at')
    return render(request, 'index.html',context={'patients':patients})

def report(request, id):
    if not request.session.get('doctor_id'):
        return redirect('login')
    patient = PatientModel.objects.get(id=id)
    return render(request, 'report.html', {'patient': patient})

def logout(request):
    if request.session.get('doctor_id'):
        try:
            del request.session['doctor_id']
            del request.session['doctor_email']
        except:
            pass
    return redirect('login')