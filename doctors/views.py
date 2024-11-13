from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import DoctorRegisterForm
from .models import Doctor


def doctor_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'doctors/logindoctor.html', {'error': 'Email ou senha incorretos'})
    return render(request, 'doctors/logindoctor.html')

def home_redirect(request):
    return redirect('doctor-login')

def doctor_register_view(request):
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            doctor = Doctor(
                name=form.cleaned_data.get('name'),
                age=form.cleaned_data.get('age'),
                gender=form.cleaned_data.get('gender'),
                crm=form.cleaned_data.get('crm'),
                email=form.cleaned_data.get('email'),
            )
            doctor.save()
            login(request, user)
            return redirect('home')
    else:
        form = DoctorRegisterForm()
        return render(request, 'doctors/register.html', {'form': form})
    
