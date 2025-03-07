from django.contrib import admin
from django.urls import include, path

from todos import views

# dev_1
urlpatterns = [
    path("", views.home, name="home"),
]
