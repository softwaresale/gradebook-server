
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.grades_list),
    path('<int:pk>/', views.grades_detail)
]
