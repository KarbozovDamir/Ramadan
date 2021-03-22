from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
# from rest_framework.response import Response
# from rest_framework.views import APIView

from .models import *

# app_name = "ramadan2021"


def index(request):
    return render(request, 'ramadan2021/index.html', {'title': 'Главная страница'})

def api(request):
    data = {
        'name': request.user.username,  # username of current logged-in user
        'skills': ['Python', 'Django'],
    }
    return JsonResponse(data)

def categories(request, catid):
    data = {
        'question': ['answer'],
    }
    return JsonResponse(data)



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


# def categories(request, catid):
#     if(request.POST):
#         print(request.POST)

#     return HttpResponse(f"<h1>Категории</h1><p>{catid}</p>")