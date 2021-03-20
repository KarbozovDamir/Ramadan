from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse


def index(request):
    return render(request, 'ramadan2021/index.html', {'title': 'Главная страница'})

def api(request):
    data = {
        'name': request.user.username,  # username of current logged-in user
        'skills': ['Python', 'Django'],
    }
    return JsonResponse(data)


def categories(request, catid):
    if(request.POST):
        print(request.POST)

    return HttpResponse(f"<h1>Категории</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
