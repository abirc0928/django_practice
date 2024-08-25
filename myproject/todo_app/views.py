from django.shortcuts import render
from .models import Task
# Create your views here.
def task_lsit(request):
    tasts = Task.objects.all()
    completed = request.GET.get("completed")
    if completed == "1":
        tasts = tasts.filter(completed = True)
    if completed == "0":
        tasts = tasts.filter(completed = False)
    return render(request, 'tast_list.html', {'tasks':tasts})

def task_details(request, pk):
    task = Task.objects.get(pk = pk)
    return render(request, 'task_datils.html', {'task':task}) 
