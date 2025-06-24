from django.shortcuts import render

from .models import Task

def home(request):
    tasks = Task.objects.all() 
    return render(request , "task_list.html", {'tasks': tasks})

def details(request,task_id):
    task = Task.objects.get(id=task_id)
    return render(request , "task_details.html", {'task': task})