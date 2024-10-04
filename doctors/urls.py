from django.urls import path
from .views import doctor_login_view

urlpatterns = [
    path('login/', doctor_login_view, name='doctor-login'), 
]