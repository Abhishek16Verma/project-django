from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("<h1>Home Page</h1>")
    restaurant = [{
        "name": "Indian Foods",
        "description": "This is Indian Restaurant"
    },
    {
        "name": "Cafe Day",
        "description": "cafe"
    }]
    return render(request, 'index.html', context={"restaurant":restaurant})

def user(request):
    return render(request, 'profile.html')