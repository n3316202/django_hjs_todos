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
]
