from django.http import HttpResponse
from django.shortcuts import redirect, render

from todos.forms import TodoForm
from todos.models import Todo

# Create your views here.


# dev_1
def home(request):
    # return HttpResponse("<h1>안녕하세요</h1>")
    return render(request, "home.html")


# dev_3


def todo_list(request):
    # select * from todos where complete=0
    todos = Todo.objects.filter(complete=True)
    print(todos)
    return render(request, "todo/todo_list.html", {"todos": todos})


def todo_post(request):

    if request.method == "POST":
        form = TodoForm(request.POST)
        
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect("todo_list")
        
    else:
        form = TodoForm()

    return render(request, "todo/todo_post.html", {"form": form})
