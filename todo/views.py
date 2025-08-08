from django.shortcuts import render, redirect
from .models import  Task
from django.views.decorators.http import require_POST
# Create your views here.

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')

    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks':tasks})

def complete_task(require, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')
