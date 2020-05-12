from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def exam_home(request):
    return render(request, 'Exam/login.html')
