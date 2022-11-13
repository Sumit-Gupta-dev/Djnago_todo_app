from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from django.db import connection
from .models import task
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.





@login_required(login_url='/signin/')
def index(request):
    if request.method == 'POST':
        get_task = request.POST.get('new-task-input')
        create_task = task.objects.create(task_data=get_task,user=request.user)
        return redirect('home')
    data = task.objects.filter(user=request.user)


    task_list = task.objects.filter(user=request.user)
    paginator = Paginator(task_list,3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    nums = 'a' * paginator.num_pages

    # print(data)
    return render(request,'index.html',context={'tasks':data, 'page_obj':page_obj, 'nums':nums})

@login_required(login_url='/signin/')
def edit_task(request,id):
    taskId = task.objects.get(id=id)
    try:
        if request.method == 'POST':
            taskSave = request.POST.get('task_edit')
            taskId.is_completed = True
            taskId.task_data = taskSave
            taskId.save()
            return redirect('home')


        return render(request, 'edit_task.html',context={'main':taskId})
    except Exception as e:
        print(e)
        return render(request, 'edit_task.html')


def delete_todo(request,id):
    delete_data = task.objects.get(id=id)
    delete_data.delete()
    return redirect('home')
    return render(request, 'delete_todo.html')



def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        userdata = User.objects.filter(username= email)
        if userdata.exists():
            messages.warning(request, 'Account Already Exits! <a href="/signin/"> Click here </a> to Login ')
            return redirect('signup')
        else:
            user = User.objects.create(username = email, first_name=first_name, last_name=last_name, email=email)
            user.set_password(password)
            user.save()
            messages.warning(request, 'Account Created! <a href="/signin/"> Click here </a> to redirect on login page ')
            return redirect('signup')
    return render(request , 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        check_data = User.objects.filter(username = email)

        if not check_data.exists():
            messages.warning(request, 'Account Not Found! ')
            return redirect('signin')
        
        login_user = authenticate(username = email, password=password)
        if login_user:
            login(request, login_user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Email Id and Password ')
            return redirect('signin')

    return render(request , 'signin.html')


def user_logout(request):
    logout(request)
    return redirect('signin')
    return render(request, 'logout.html')





def search_task(request):
    if request.method == "POST":
        query = request.POST.get('search_data')
        
        data = task.objects.filter(task_data__icontains = query)
        return render(request, 'search.html', context={'searchs':data} )
        
    else:
        messages.warning(request, 'Enter Your Search')
        return render(request, 'search.html')