from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import acc_questions

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
    allQuestions = acc_questions.objects.all()
    context = {'allQuestions': allQuestions}
    return render(request, 'Exam/questions.html',context)
