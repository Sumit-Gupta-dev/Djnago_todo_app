from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from django.db import connection
from .models import task
# Create your views here.






def index(request):
    if request.method == 'POST':
        task_data = request.POST.get('new-task-input')
        create_task = task.objects.create(task_data=task_data)
        return redirect('home')
    data = task.objects.all().values
    return render(request,'index.html',context={'tasks':data})


def edit_task(request,id):
    taskId = task.objects.get(id=id)
    if request.method == 'POST':
        taskSave = request.POST.get('task_edit')
        taskId.task_data = taskSave
        taskId.save()
        return redirect('home')


    return render(request, 'edit_task.html',context={'main':taskId})


def delete_todo(request,id):
    delete_data = task.objects.get(id=id)
    delete_data.delete()
    return redirect('home')
    return render(request, 'delete_todo.html')











