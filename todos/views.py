from django.http import HttpResponse
from django.shortcuts import redirect, render

from todos.forms import TodoForm
from todos.models import Todo

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.views import APIView

from todos.serializers import TodoDRFSerializer
from rest_framework import status

# Create your views here.


# dev_7
# DRF 방식
# @api_view(["GET"])
# def todo_drf(request):
#    return Response({"message": "Hello World!"})

# API => 함수 => json,xml(데이타) 가져오는(호출) 함수


class TodoAPIView(APIView):
    def get(self, request):

        todos = Todo.objects.all()

        print(todos)
        # querySet 리턴일 경우 many=True 설정
        serializer = TodoDRFSerializer(todos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass


# def todo_drf(request):
#    return JsonResponse({"message": "Hello World!"})


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


def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    # todo.title = "하하하"
    # todo.description = "메롱"
    todo.save()
    return redirect("todo_list")


# redirect 하고 forward 의 차이


def done_list(request):
    # select * from todos where complete=1
    dones = Todo.objects.filter(complete=True)
    print(dones)
    return render(request, "todo/done_list.html", {"dones": dones})
