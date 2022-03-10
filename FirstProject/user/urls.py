from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from . import views

# http://localhost/user
app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register')
]
