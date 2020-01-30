from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('course/', views.course_today),
    path('course/<int:id>/', views.course_detail),
    path('course/check/', views.course_check)
]