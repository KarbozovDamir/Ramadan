from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse

from .models import *

# app_name = "ramadan2021"


def index(request):
    posts = Answer.objects.all()
    # category = Category.objects.all()

    return render(request, 'ramadan2021/index.html', {'posts': posts, 'title': 'Главная страница'})

def api(request):
    data = {
        'name': request.user.username, 
        'skills': ['Python', 'Django'],
    }
    return JsonResponse(data)

def answer(request, answer_id):
    return render(request, 'ramadan2021/answer.html', {'title': 'Ответы'})

def categories(request, catid):
    return render(request, 'ramadan2021/categories.html', {'title': 'Категории'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

#  def categories(request, catid):
#     if(request.POST):
#         print(request.POST)

#     return HttpResponse(f"<h1>Категории</h1><p>{catid}</p>")

# def show_post(request, post_id)
#     return HttpResponse(f"Отображение ответов c id = {post_id}")

# def show_category(request, cat_id)
#     return HttpResponse(f"Отображение Категории c id = {post_id}")