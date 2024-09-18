from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),  
    path('patient/new/', views.patient_create, name='patient_create'), 
    path('patient/<int:pk>/', views.patient_detail, name='patient_detail'), 
    path('patient/<int:pk>/edit/', views.patient_update, name='patient_update'), 
    path('patient/<int:pk>/delete/', views.patient_delete, name='patient_delete'),  
]