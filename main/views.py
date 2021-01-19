from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request,"test.html")

def second(request):
    return HttpResponse("test 2 page")


def homework(request):
    return render(request, "homework31.html")

def homework2(request):
    return render(request, "homework312.html")

def homework3(request):
    return render(request, "homework3.html")


# def third(request):
#     return HttpResponse("This is page test3.")