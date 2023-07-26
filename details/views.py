from django.shortcuts import render, redirect
from .models import TodoList
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":        
        data=request.POST["txt"]
        my_task=TodoList(task=data)
        my_task.save()
        messages.success(request,"Item added")

    return render(request, 'index.html')


def show(request):
    data=TodoList.objects.all()
    return render(request, 'display.html', {'myinfo':data})

def delete(request, task):
    my_task=TodoList.objects.get(task=task)
    my_task.delete()
    messages.success(request, "Task deleted successfully")
    return redirect('http://127.0.0.1:8000/display')
