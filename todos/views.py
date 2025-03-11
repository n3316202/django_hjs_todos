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
    todos = Todo.objects.filter(complete=False)
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


# http://127.0.0.1:8000/todo/{1}/ + GET, POST, PUT, DELETE, OPTION
# path("<int:pk>", views.todo_detail, name="todo_detail"),  # dev_4
def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)  # filter는 1개이상,get=1개만 꺼내옴
    return render(request, "todo/todo_detail.html", {"todo": todo})


# dev_5
def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            # SQL 실행시킨 상태이지만 = 메모리에만 올려놓고 영구저장(commit)은 안한상태
            todo = form.save(commit=False)
            todo.save()
            return redirect("todo_list")
    else:
        form = TodoForm(instance=todo)  # 레코드,튜플,행 #

    return render(request, "todo/todo_post.html", {"form": form})
