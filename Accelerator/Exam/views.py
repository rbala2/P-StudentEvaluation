from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import AccQuestions,AccTests,AccTestQuestions
from .forms import QuestionForm

# Create your views here.

def student_login(request):
    return render(request, 'Exam/login.html')


def exam_home(request):
    context = {'full_name': ''}

    if request.method == 'POST' and request.POST is not None:
        usr_instance = authenticate(username=request.POST['email'], password=request.POST['password'])
        if usr_instance is not None:
            context['fullname'] = usr_instance.first_name.capitalize() + ', ' + usr_instance.last_name.capitalize()
            request.session['member'] = usr_instance.username
            request.session['fullname'] = context['fullname']
            response = render(request, 'Exam/base.html', context)
            response.set_cookie(key='id', value=usr_instance.username)
            return response
        else:
            return render(request, 'Exam/errorpage.html')
    else:
        if request.session.get('member', 'NA') != "NA" and \
                request.COOKIES.get('id') == request.session.get('member', 'NA'):
            return render(request, 'Exam/base.html', {'fullname': request.session['fullname']})
        return render(request, 'Exam/errorpage.html')


def student_logout(request):
    del request.session['member']
    del request.session['fullname']
    return render(request, 'Exam/logout.html')

def getQuestions(request):
    test_id = request.GET['test_id']
    total_questions = request.GET["ques_cnt"]
    allQuestions = AccTestQuestions.objects.all().filter(test_id=test_id)
    context = {'allQuestions': allQuestions,'tot_ques': total_questions}
    return render(request, 'Exam/questions.html',context)

def GetTests(request):
    all_tests = AccTests.objects.all()
    ctx = {'all_tests':all_tests}
    return render(request, 'Exam/tests.html', ctx)

def PostQuestions(request):
    form = QuestionForm()
    return render(request, 'Exam/post_questions.html', {'form': form})
