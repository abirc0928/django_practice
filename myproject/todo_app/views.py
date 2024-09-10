from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Task, Book, Author
from .forms import TaskForm

from django.contrib.auth.models import User
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
            

def task_by_user_id(request, user_id):
    ############ 1st way to read data #####

    #---------------- all data -----------
    # tasks = Task.objects.all().values()
    # return JsonResponse({"tasks": list(tasks)})

    #---------------- filter by user id -----------
    # tasks = Task.objects.filter(user_id = user_id).values()
    # return JsonResponse({"tasks": list(tasks)})


    ############ 2nd way to read data #####
    #---------------- task gola age ber korcii --------------
    # tasks = Task.objects.filter(user_id = user_id)
    # result = []
    # for task in tasks:
    #     result.append({
    #         "title": task.title,
    #         "description": task.description,
    #         "completed" : task.completed,
    #         "create_at": task.create_at,
    #         "due_data": task.due_data,
    #         "user_id": task.user.id,
    #         "user": task.user.first_name
    #     }) 
    # return JsonResponse({"tasks": result})

    
    ############ 3rd way to read data #####
    user = User.objects.get(pk=user_id)
    tasks = user.tasks.all().values()
    return JsonResponse({"tasks": list(tasks)})

#------- relation between book to author it is one to one relation ------------   
    ############# all books ################
def all_books(request):
    #------------ one way ----------
    # books = Book.objects.all().values()
    # return JsonResponse({"tasks": list(books)})

    #------------ one way ----------
    books = Book.objects.all()
    print(books)
    result = []
    for book in books:
        result.append({
            "title": book.title,
            "description" : book.description,
            "publication_date": book.publication_date,
            "author" :f"{book.author.first_name} {book.author.last_name}" 
        })
   
    return JsonResponse({"tasks": result})

#------- relation between book to author it is one to one relation ------------
############# single book ################

# def book(request, book_id):
#     book = Book.objects.get(pk=book_id)
#     book_details ={
#         "title": book.title,
#         "description" : book.description,
#         "publication_date": book.publication_date,
#         "author" :f"{book.author.first_name} {book.author.last_name}" 
#     }
#     return JsonResponse({"tasks": book_details})

# #------- relation between author to book it is one to many relation ------------
def author(request, author_id):
    author = Author.objects.get(pk = author_id)

    author_details ={
        "first_name": author.first_name,
        "last_name" : author.last_name,
        "bio":author.bio,
        "books":[book.title for book in author.books.all()]
    }
    return JsonResponse({"tasks": author_details})

# --------------- many to many ---------

def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book_details = {
        "title": book.title,
        "description": book.description,
        "publication_date": book.publication_date,
        "author": [
            f"{author.first_name} {author.last_name}"
            for author in book.author.all()
        ],
    }
    return JsonResponse({"book": book_details})

def all_books(request):
    books = Book.objects.all()
    # return JsonResponse({"books": list(books)})
    result = []
    for book in books:
        result.append(
            {
                "title": book.title,
                "description": book.description,
                "publication_date": book.publication_date,
                # "author_ids":[
                #    ) author.id for author in book.author.all(
                # ],
                # "author": [
                #     f"{author.first_name} {author.last_name}"
                #     for author in book.author.all()
                # ]
                "authors":[
                    {
                        "id":author.id,
                        "first_name":author.first_name,
                        "last_name":author.last_name
                    } for author in book.author.all()
                ]
            }
        )

    return JsonResponse({"books": result})

