from django.contrib import admin
from django.urls import include, path

# http://127.0.0.1:8000/admin
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todos.urls")),  # dev_1
]
