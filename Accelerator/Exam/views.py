from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import AccQuestions, AccTests, AccTestQuestions, AccResults
from .forms import QuestionForm
from django.views.generic import ListView
import datetime, pytz


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

def exam_board(request):
    return render(request, 'Exam/examboard.html')

def test_complete(request):
    cnt=1
    obj = AccResults()
    ctxt = dict(zip(request.POST.keys(), request.POST.values()))
    del ctxt['csrfmiddlewaretoken']
    #del ctxt['test_start_time']
    for ky,val in ctxt.items():
        if ky != 'csrfmiddlewaretoken':
            obj.id = cnt
            obj.login_id = request.session['member']
            obj.session_id = request.POST['csrfmiddlewaretoken']
            obj.testid = 1
            obj.qno = int(ky)
            obj.qtype = 'OBJ'
            obj.answer_obj = val
            obj.test_starttime = request.COOKIES.get('start_time')
            obj.test_endtime = datetime.datetime.now()
            obj.save()
            cnt += 1
    return render(request, 'Exam/questions.html', {'ctxt': ctxt})


class QuestionsView(ListView):
    model = AccQuestions

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['start_time'] = datetime.datetime.now()
    #     return context

    def render_to_response(self, context, **response_kwargs):
        response = super(QuestionsView, self).render_to_response(context, **response_kwargs)
        response.set_cookie("start_time",datetime.datetime.now().astimezone(pytz.timezone('Asia/Calcutta')))
        return response
