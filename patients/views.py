from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm
from django.contrib import messages


