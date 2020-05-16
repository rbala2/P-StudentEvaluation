from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


# Create your views here.

def student_login(request):
    return render(request, 'Exam/login.html')


def exam_home(request):
    return render(request, 'Exam/base.html')
