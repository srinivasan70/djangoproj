from django.contrib import admin
from django.urls import path
from loginapp import views

urlpatterns = [
    path('post/', views.post_login),
    path('getdetails/',views.get_login)
]
