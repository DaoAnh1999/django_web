from django.shortcuts import render, redirect, get_object_or_404
from .models import (Task, User)
from django.views.generic import ListView
from .models import Task

class Login():
    def home(request):
        if 'user' in request.session:
            return redirect('task-list')
        else:
            return redirect('login')
        return render(request, 'base.html')

    def signup(request):
        if request.method == 'POST':
            uname = request.POST.get('uname')
            pwd = request.POST.get('pwd')

            if User.objects.filter(username=uname).count()>0:
                return render(request, 'signup.html', {'message':'Username already exists. Please fill another username.'})
            else:
                user = User(username=uname, password = pwd)
                user.save()
                return render(request, 'login.html',{'message':'Register username sucessfully. Please login.'})  
        else:
            return render(request, 'signup.html',{'message':""})         
        
    def login(request):
        if request.method == 'POST':
            uname = request.POST.get('uname')
            pwd = request.POST.get('pwd')
            check_user = User.objects.filter(username=uname, password = pwd)
            if uname=='' or pwd=='':
                return render(request, 'login.html', {'message':'Please fill username and password.'})
            else:
                if check_user:
                    request.session['user'] = uname
                    return redirect('task-list')
                else:
                    return render(request, 'login.html', {'message':'username or password is incorrect.'})
        return render(request, 'login.html', {'message':''})

    def logout(request):
        try:
            del request.session['user']
        except:
            return redirect('login')
        return redirect('login')

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def create_task(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            deadline = request.POST.get('deadline')
            status = request.POST.get('status')

            task = Task(title=title, description=description, deadline=deadline, status=status)
            task.save()
            return redirect('task-list')

        return render(request, 'task_create.html')

    def update_task(request, pk): 
        task = get_object_or_404(Task, pk=pk)

        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            deadline = request.POST.get('deadline')
            status = request.POST.get('status')

            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if deadline: 
                task.deadline = deadline
            if status is not None:
                task.status = status

            task.save()
            return redirect('task-list') 

        return render(request, 'task_update.html', {'task': task})

    def search_tasks(request):
        query = request.GET.get('q')
        tasks = Task.objects.filter(title__icontains=query)
        return render(request, 'task_list.html', {'tasks': tasks})

    def delete_task(request, pk):
        task = get_object_or_404(Task, pk=pk)
        
        if request.method == 'POST':
            task.delete()
            return redirect('task-list')
        
        return render(request, 'confirm_delete.html', {'task': task})

