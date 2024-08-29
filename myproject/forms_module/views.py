from django.shortcuts import render, redirect
from .forms2 import SearchForm, AddTodoForm
from .models import Todo

# def form(request):
#     todos = [
#         {"title": "Buy groceries", "completed": False},
#         {"title": "Do laundry", "completed": False},
#         {"title": "Clean Balcony", "completed": True},
#     ]

#     search_form = SearchForm(request.POST)
#     search_term = ""
#     if search_form.is_valid():
#         search_term = search_form.cleaned_data["query"]


#     searched_todo = []
#     for todo in todos:
#         if search_term and search_term in todo.get("title").lower():
#             searched_todo.append(todo)


#     context = {
#         "search_form": search_form,
#         "todos": searched_todo
#         }
#     return render(request, "form.html", context)


def todos(request):
    if request.method == "POST":
        add_todo_form = AddTodoForm(request.POST)
        if add_todo_form.is_valid():
            add_todo_form.save()
        return redirect("todos")   

    add_todo_form = AddTodoForm()
    todos = Todo.objects.all()

    context = {"todos": todos, "add_todo_form": add_todo_form}
    return render(request, "form.html", context)
