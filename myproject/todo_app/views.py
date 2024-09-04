from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.
def task_lsit(request):
    tasts = Task.objects.all()
    completed = request.GET.get("completed")
    if completed == "1":
        tasts = tasts.filter(completed = True) #filter data
    if completed == "0":
        tasts = tasts.filter(completed = False) #filter data
    return render(request, 'tast_list.html', {'tasks':tasts})

def task_details(request, pk):
    try:
        task = Task.objects.get(pk = pk)
        return render(request, 'task_datils.html', {'task':task}) 
    except task.DoesNotExist:
        return HttpResponse("Task does not exit")

def add_task(request):
    _title = "Let's have dinner together "
    _description = "Dinner invitation at Chefs Table "
    _completed = True
    _due_date = "2024-08-28"

    task = Task(title=_title, description= _description, completed=_completed, due_data=_due_date)
    task.save()
    return redirect("task_lsit")

def delete_task(request, pk):
    try:
        task = Task.objects.get(pk = pk)
        task.delete()
    except Task.DoesNotExist:
        return HttpResponse("Task does not exist")
    return redirect("task_lsit")

def update_task(request, pk):
    task = Task.objects.get(pk = pk)
    task.title = "updated task"
    task.save()
    return redirect("task_lsit")

def add_task_form(request):
    if request.method == "POST":
        add_todo_form = TaskForm(request.POST)
        if add_todo_form.is_valid():
            add_todo_form.save()
            return redirect("task_lsit")
        else:
            return render(request, "add_task.html", {"form":add_todo_form})
            

    add_todo_form = TaskForm()
    context = {
        "form": add_todo_form,
    }
    return render(request, "add_task.html", context)

def update_task_form(request, pk):
    try:
        task = Task.objects.get(pk = pk)
        if request.method == "POST":
            task_form = TaskForm(request.POST, instance=task)
            if task_form.is_valid():
                task_form.save()
                return redirect("task_lsit")
            else:
                return render(request, "update_task_form.html", {"form":task_form})

        task_form = TaskForm(instance=task)
        return render(request, "update_task_form.html", {"form":task_form})
        
    except Task.DoesNotExist:
        return HttpResponse("Task does not exist")
    