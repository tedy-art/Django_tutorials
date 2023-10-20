from django.shortcuts import render, redirect

from .forms import ContactFrom, TaskForm
from .models import Task, Tag


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        content = request.POST['content']
        deadline = request.POST['deadline']
        task = Task(content=content, deadline=deadline)
        task.save()
        return redirect('tasks')
    else:
        return render(request, 'tasks/new_task.html')

def add_task_2(request):
    if request.method == 'POST':
        form = TaskForm(data = request.POST)
        if form.is_valid():
            new_task = form.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/new_task_2.html', {'form':form})

def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        # send the email
        return redirect('tasks')
    else:
        return render(request, 'tasks/contact_us.html')


def contact_2(request):
    if request.method == 'POST':
        form = ContactFrom(data=request.POST)
        if form.is_valid():
            # send mail
            return redirect('tasks')
    else:
        form = ContactFrom()
    return render(request, 'tasks/contact_us_2.html', {'form': form})
