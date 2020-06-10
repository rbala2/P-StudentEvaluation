from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout_then_login
from .models import AccQuestions, AccTests, AccTestQuestions, AccStudentTests
from .forms import QuestionForm


# Create your views here.

def student_login(request):
    return render(request, 'Exam/login.html')


def exam_home(request):
    context = {'full_name': ''}

    if request.method == 'POST' and request.POST is not None:
        usr_instance = authenticate(username=request.POST['email'], password=request.POST['password'])
        if usr_instance is not None:
            login(request, usr_instance)
            context['fullname'] = usr_instance.get_full_name()
            request.session['member'] = usr_instance.username
            request.session['fullname'] = context['fullname']
            response = render(request, 'Exam/base.html', context)
            response.set_cookie(key='id', value=usr_instance.username)
            return response
        else:
            messages.error(request, "Password not match")
            return render(request, 'Exam/login.html')
    else:
        if request.session.get('member', 'NA') != "NA" and \
                request.COOKIES.get('id') == request.session.get('member', 'NA'):
            return render(request, 'Exam/base.html', {'fullname': request.session['fullname']})
        return render(request, 'Exam/errorpage.html')


def student_logout(request):
    logout(request)
    # del request.session['member']
    # del request.session['fullname']
    return logout_then_login(request, login_url="/Exam/StudentLogin")
    # return render(request, 'Exam/logout.html')


def get_questions(request, test_id, ques_cnt):
    all_questions = AccTestQuestions.objects.all().filter(test_id=test_id)
    context = {'allQuestions': all_questions, 'tot_ques': ques_cnt}
    return render(request, 'Exam/questions.html', context)


def get_tests(request):
    all_tests = AccStudentTests.objects.all().filter(student_id=3)
    ctx = {'all_tests': all_tests}
    return render(request, 'Exam/tests.html', ctx)


def post_questions(request):
    form = QuestionForm()
    return render(request, 'Exam/post_questions.html', {'form': form})
