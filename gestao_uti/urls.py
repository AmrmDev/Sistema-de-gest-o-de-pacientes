from django.contrib import admin
from django.urls import path, include
from doctors.views import doctor_login_view, home_redirect

urlpatterns = [
    path('', home_redirect, name='home'),
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),
    path('login/', doctor_login_view, name='doctor-login'),
    path('doctors/', include('doctors.urls')),
]
