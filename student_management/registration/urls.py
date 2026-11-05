from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.student_registration, name='register'),
    path('success/', views.registration_success, name='registration_success')
]