from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, decorators
from django.contrib.auth.views import logout_then_login
from django.views.generic import ListView
from .models import AccQuestions, AccTests, AccTestQuestions, AccStudentTests, AccResults
from .forms import QuestionForm
from  datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

from . import utilities
# Create your views here.


def student_login(request):
    if request.session.get('member', 'NA') != "NA" and \
            request.COOKIES.get('id') == request.session.get('member', 'NA'):
        return redirect('exam-home')
    return render(request, 'Exam/login.html')


# @decorators.login_required(login_url='student-login')
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
            # messages.error(request, "Password not match")
            return render(request, 'Exam/login.html')
    else:
        if request.session.get('member', 'NA') != "NA" and \
                request.COOKIES.get('id') == request.session.get('member', 'NA'):
            return render(request, 'Exam/base.html', {'fullname': request.session['fullname']})
        return render(request, 'Exam/errorpage.html')


def student_logout(request):
    logout(request)
    return logout_then_login(request, login_url="student-login")


# def get_questions(request, test_id, ques_cnt):
#     all_questions = AccTestQuestions.objects.all().filter(test_id=test_id)
#     context = {'allQuestions': all_questions, 'tot_ques': ques_cnt}
#     return render(request, 'Exam/questions_unused.html', context)


@decorators.login_required(login_url='student-login')
def get_tests(request):
    all_tests = AccStudentTests.objects.all().filter(student_id=request.user.id)
    ctx = {'all_tests': all_tests}
    return render(request, 'Exam/tests.html', ctx)


def post_questions(request):
    form = QuestionForm()
    return render(request, 'Exam/post_questions.html', {'form': form})


def test_complete(request):
    cnt=1
    obj = AccResults()
    tobj = AccStudentTests.objects.get(student_id=request.user.id, test_id=request.COOKIES['test_id'])
    if tobj.test_status == 'Completed':
        return render(request, 'Exam/errorpage.html')

    # tobj = AccStudentTests.objects.get(student_id=request.user.id,test_id=request.COOKIES['test_id'])
    ctxt = dict(zip(request.POST.keys(), request.POST.values()))
    del ctxt['csrfmiddlewaretoken']
    # del ctxt['test_start_time']

    if len(ctxt) == 0:
        tobj.test_status = 'Attempted'
        tobj.save()
        del request.session["exam_start_time"]
        return redirect('exam-home')

    for ky,val in ctxt.items():
        if ky != 'csrfmiddlewaretoken':
            # obj.id = cnt
            obj.pk = None
            obj.student_id = request.user.id
            obj.login_id = request.session['member']
            obj.session_id = request.POST['csrfmiddlewaretoken']
            obj.testid = request.COOKIES['test_id']
            obj.qno = int(ky)
            obj.qtype = 'OBJ'
            obj.answer_obj = val
            # obj.test_starttime = request.COOKIES['exam_start_time']
            obj.test_starttime = request.session['exam_start_time']
            obj.test_endtime = datetime.now()
            obj.save()
            cnt += 1
    #return render(request, 'Exam/base.html', {'ctxt': ctxt})
    tobj.test_status = 'Completed'
    tobj.save()
    # exam evaluation
    utilities.evaluate_exam(request.user.id,request.POST['csrfmiddlewaretoken'],request.COOKIES['test_id'])
    del request.session["exam_start_time"]
    return redirect('exam-home')


@method_decorator(never_cache, name='dispatch')
class QuestionsView(ListView):
    # model = AccQuestions
    template_name = 'Exam/questions.html'

    # def get(self, request, **response_kwargs):
    #     model = AccQuestions.objects.all()
    #     return render(request, 'Exam/questions.html')

    def get_context_data(self, **ctx_kwargs):
        context = super().get_context_data(**ctx_kwargs)
        context['ques_cnt'] = self.kwargs['ques_cnt']
        context['exam_desc'] = self.request.COOKIES['exam_desc']
        context['exam_dur'] = self.request.COOKIES['exam_dur']
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super(QuestionsView, self).render_to_response(context, **response_kwargs)
        response.set_cookie("test_id", self.kwargs['test_id'])
        # response.set_cookie("exam_start_time", datetime.now())
        if self.request.session.get("exam_start_time", 'NA') == 'NA':
            self.request.session["exam_start_time"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        else:
            del self.request.session["exam_start_time"]
            return redirect('exam-home')

        # response.set_cookie("exam_desc", self.request.COOKIES['exam_desc'])
        tobj = AccStudentTests.objects.get(student_id=self.request.user.id, test_id=self.kwargs['test_id'])
        # if self.request.COOKIES['exam_dur'] == '-1':
        if tobj.test_status == 'Attempted':
            del self.request.session["exam_start_time"]
            return redirect('exam-home')
        else:
            # tobj = AccStudentTests.objects.get(student_id=self.request.user.id, test_id=self.kwargs['test_id'])
            tobj.test_status = 'Attempted'
            tobj.save()
            # response.set_cookie("exam_dur", '-1')
        return response

    def get_queryset(self):
        qus = AccTestQuestions.objects.filter(test_id_id=self.kwargs['test_id'])
        return AccQuestions.objects.filter(qno__in=qus.values('question_id_id'))
