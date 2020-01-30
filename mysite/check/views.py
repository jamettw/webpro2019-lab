from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course_today(request):
    return HttpResponse('หน้าจอรายการวิชาที่มีการสอนในวันนั้น ๆ ของ อ. ที่ login เข้ามา')

def course_detail(request, id):
    return HttpResponse("หน้าจอรายละเอียดของแต่ละวิชา (วิชานี้สอนอะไร, มีจำนวนนักเรียนกี่คน, มีคนมาเรียน และขาดกี่คน) %d" %id)

def course_check(request):
    return HttpResponse("หน้าจอเช็คชื่อของแต่ละวิชาที่สามารถเช็คชื่อได้ด้วย QR code")