"""Accelerator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('ExamHome', views.exam_home, name='exam-home'),
    path('StudentLogin/', views.student_login, name='student-login'),
    path('StudentLogout/', views.student_logout, name='student-logout'),
    path('PostQuestions', views.post_questions, name='post-questions'),
    path('GetTests', views.get_tests, name='get-tests'),
    re_path(r'^GetQuestions/(?P<test_id>\w+)/(?P<ques_cnt>\w+)/$', views.get_questions,name='get-questions'),
    path('TestComplete/', views.test_complete, name='test-complete'),
    path('GetQuestions/', views.QuestionsView.as_view(), name='get-questions'),
    path('Examboard/', views.exam_board, name='exam-board'),

]
