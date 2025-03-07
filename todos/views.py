from django.shortcuts import render

# Create your views here.


# dev_1
def home(request):
    return render(request, "home.html")
