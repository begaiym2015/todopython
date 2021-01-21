from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request,"test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")


def homework(request):
    return render(request, "homework31.html")

def homework2(request):
    return render(request, "homework312.html")

def books(request):
    return render(request, "books.html")


# def third(request):
#     return HttpResponse("This is page test3.")