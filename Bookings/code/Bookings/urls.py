"""Bookings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='Home-Page'),
    path('add/',views.add, name='Add-Booking'),
    path('details/<int:pk>/',views.details, name='Booking-Details'),
    path('edit/<int:pk>/',views.edit, name='Edit-Bookings'),
    path('logout/',views.logout_view,name='logout'),
    
    path('delete/<int:pk>/',views.delete, name='Delete-Bookings'),
    path('add_address/<int:pk>/',views.add_address, name='Add-address'),
    path('add_phone/<int:pk>/',views.add_phone, name='Add-phone'),
    path('add_booking/<int:pk>/',views.add_booking, name='Add-booking'),
    path('add_contact/',views.add_contact, name='Add-contact'),
    path('update_booking/<int:pk1>/<int:pk2>/',views.update_booking, name='Update-Bookings'),
    path('change_booking/<int:pk1>/<int:pk2>/',views.change_booking, name='Change-Bookings'),
    
]
