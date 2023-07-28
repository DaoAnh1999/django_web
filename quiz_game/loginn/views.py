from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.views.decorators.cache import cache_page
from django.core.cache import caches
from django.core.cache.backends.base import InvalidCacheBackendError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import forms
from .forms import Input
from .models import Question
# Create your views here.

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'base.html', param)
    else:
        return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        if User.objects.filter(username=uname).count()>0:
            return HttpResponse("Username already exists.")
        else:
            user = User(username=uname, password = pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')         
    
def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
    
        check_user = User.objects.filter(username=uname, password = pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('home')
        else:
            return HttpResponse('Plesase enter valid username or password.')
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')

def nhapcau(request):
    input = forms.Input()
    if request.method == 'POST':
        input = forms.Input(request.POST)
        if input <= 10 and input > 0:
            cauhoi()
        else:
            message = 'khong dung gia tri'
    else:
        message = 'Input number question!'
    return render(request, 'input.html', {'message':message, 'input':input})

def cauhoi(request):
    # def cauhoi(request, input):
    try:
        question_list = caches['question_list']
        print(f'getdatafromcache{question_list}')
    except InvalidCacheBackendError :
        # question_list = Question.objects.range[0,input]
        question_list = Question.objects.all()
        caches['question_list'] = question_list
        print(f'getdatadatabase{question_list}')

    paginator = Paginator(question_list, 2)
    pageNumber = request.GET.get('page')
    try:
        questions = paginator.page(pageNumber)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'pagination_1.html', {'questions':questions})
