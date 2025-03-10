from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# dev_1
def home(request):
    #return HttpResponse("<h1>안녕하세요</h1>")
    return render(request, "home.html")
