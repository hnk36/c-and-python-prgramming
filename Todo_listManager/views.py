from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, SubTask, Comment
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login as auth_login, authenticate

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('task_list')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'register.html')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    if request.method == 'POST':
        if 'task_title' in request.POST:
            title = request.POST['task_title']
            description = request.POST.get('task_description', '')
            priority = request.POST.get('task_priority', 'L')
            Task.objects.create(user=request.user, title=title, description=description, priority=priority)
        elif 'subtask_title' in request.POST:
            task_id = request.POST['task_id']
            task = get_object_or_404(Task, id=task_id, user=request.user)
            title = request.POST['subtask_title']
            SubTask.objects.create(task=task, title=title)
        elif 'comment_text' in request.POST:
            task_id = request.POST['task_id']
            task = get_object_or_404(Task, id=task_id, user=request.user)
            comment_text = request.POST['comment_text']
            Comment.objects.create(task=task, user=request.user, comment_text=comment_text)
        return redirect('task_list')
    elif request.method == 'DELETE':
        task_id = request.GET.get('task_id')
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.delete()
        return JsonResponse({'status': 'success'})
    return render(request, 'todo_list.html', {'tasks': tasks})


