from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, decorators
from django.contrib.auth.views import logout_then_login
from django.views.generic import ListView, CreateView
from .models import AccTestUploads


# Create your views here.
# @decorator    s.login_required(login_url='central-login')
def home(request):
    if request.method == 'POST' and request.POST is not None:
        usr_instance = authenticate(username=request.POST['username'], password=request.POST['password'])
        if usr_instance is not None:
            login(request, usr_instance)
            request.session['member'] = usr_instance.username
            first_name = usr_instance.first_name
            request.session['fname'] = first_name
            response = render(request, 'Central/base.html', locals())
            return response
        else:
            return render(request, 'Central/login.html')
    else:
        if is_valid_session(request):
            first_name = request.session['fname']
            response = render(request, 'Central/base.html', locals())
            return response
        return render(request, 'Central/login.html')


def is_valid_session(request):
    return request.session.get('member', 'NA') != 'NA'


def admin_login(request):
    if is_valid_session(request):
        return redirect('central-home')
    return render(request, 'Central/login.html')


def admin_logout(request):
    request.session['member'] = ''
    logout(request)
    return logout_then_login(request, login_url="central-login")


def bulk_upload(request):
    return render(request,'Central/questions.html')


class TestUploadView(CreateView):
    model = AccTestUploads
    template_name = 'Central/questions.html'
    fields = {'file'}
