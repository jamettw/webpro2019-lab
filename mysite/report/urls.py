from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard),
    path('dashboard/find/', views.find)
]