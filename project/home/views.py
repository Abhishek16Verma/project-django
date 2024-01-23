from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("<h1>Home Page</h1>")
    return render(request, 'index.html')

def page(request):
    return HttpResponse("<h2>Enter my page</h2>")