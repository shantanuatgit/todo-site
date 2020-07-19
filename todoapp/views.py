from django.shortcuts import render,redirect
from .models import ToDoList
from django.contrib import messages
# Create your views here.

def home(request):
    lists=ToDoList.objects.order_by("date")
    if request.method=='POST':
        if request.POST['task'] and request.POST['category']:
            list=ToDoList()
            list.task=request.POST['task']
            list.category=request.POST['category']
            list.date=request.POST['date']
            list.time=request.POST['time']
            list.save()
            lists=ToDoList.objects.order_by("date")
            messages.success(request,'Task added to your List.')
            return render(request,'home.html',{'lists':lists})
    else:
        return render(request,'home.html',{'lists':lists})


def delete(request,pk):
    item=ToDoList.objects.get(id=pk)
    item.delete()
    return redirect('/')
