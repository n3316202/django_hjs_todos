from django.contrib import admin
from django.urls import include, path

from todos import views


# dev_1
urlpatterns = [
    path("", views.todo_list, name="todo_list"),  # dev_3
    path("post/", views.todo_post, name="todo_post"),  # dev_3
    # http://127.0.0.1:8000/todo?number=1&name=ghldkf
    # http://127.0.0.1:8000/todo/{1}/ + GET, POST, PUT, DELETE, OPTION
    path("<int:pk>", views.todo_detail, name="todo_detail"),  # dev_4
    # http://127.0.0.1:8000/todo/1/edit/
    path("<int:pk>/edit", views.todo_edit, name="todo_edit"),  # dev_5
    # http://127.0.0.1:8000/todo/done/
    path("done/", views.done_list, name="done_list"),  # dev_6
    path("done/<int:pk>", views.todo_done, name="todo_done"),  # dev_6
    # path("drf/", views.todo_drf, name="todo_drf"),  # dev_7
    path("drf/", views.TodoAPIView.as_view(), name="todo_drf"),
]
