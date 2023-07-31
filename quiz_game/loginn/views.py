from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.views.decorators.cache import cache_page
from django.core.cache import caches
from django.core.cache.backends.base import InvalidCacheBackendError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Value
# from . import forms
# from .forms import Input
from .models import Question, Input
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
    mess = ''
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        mess = ''
        check_user = User.objects.filter(username=uname, password = pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('nhapcau')
        else:
            mess = 'username or password is incorrect'
            return render(request, 'login.html', {'mess':mess})
    return render(request, 'login.html', {'mess':mess})

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')

a = 0
def nhapcau(request):
    mess1 = ''
    if request.method == 'POST':
        input = request.POST.get('number')
        if input != '':
            if int(input) > 0 and int(input) < 11:
                F = int(input)
                return redirect('cauhoi')
            else:
                mess1 = 'Số lượng câu hỏi phải lớn hơn 0 và tối đa 10 '
                return render(request, 'input.html', {'mess1':mess1})
        else:
            mess1 = 'Nhap vao so luong cau hoi'
            return render(request, 'input.html', {'mess1':mess1})
    else:
        return render(request, 'input.html', {'mess1':mess1})
print(f"so F la {F, type(F)}")
def cauhoi(request):
    # def cauhoi(request, number):
    try:
        question_list = caches['question_list']
        print(f'getdatafromcache{question_list}')
    except InvalidCacheBackendError :
        #question_list = Question.objects.all()[0:number]
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
