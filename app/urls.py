from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    
    path('',views.check, name="check"),
    # path('check/',views.check,name='check'),
]