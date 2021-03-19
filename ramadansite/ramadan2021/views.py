from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return render(request, 'ramadan2021/index.html')

def categories(request, catid):
    if(request.POST):
        print(request.POST)

    return HttpResponse(f"<h1>Категории</h1><p>{catid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
