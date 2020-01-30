from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('manage/all-std/', views.all_std),
    path('manage/add-std/', views.add_std),
    path('manage/edit-std/', views.edit_std),
    path('manage/all-course/', views.all_course),
    path('manage/add-course/', views.add_course),
    path('manage/edit-course/', views.edit_course)
]