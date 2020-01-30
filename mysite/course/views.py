from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_std(request):
    return HttpResponse('หน้าจอรายการนักเรียนทั้งหมด')

def add_std(request):
    return HttpResponse('หน้าจอเพิ่มนักเรียน')

def edit_std(request):
    return HttpResponse('หน้าจอแก้ไขข้อมูลนักเรียน')

def all_course(request):
    return HttpResponse('หน้าจอรายการวิชาเรียนทั้งหมด')

def add_course(request):
    return HttpResponse('หน้าจอเพิ่มวิชาเรียน')

def edit_course(request):
    return HttpResponse('หน้าจอแก้ไขข้อมูลวิชาเรียน')