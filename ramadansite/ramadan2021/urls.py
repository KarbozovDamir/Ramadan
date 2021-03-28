from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('api/categories/', api, name='api'),
    path('api/categories/<int:catid>/', categories, name='categories'),
    path('categories/', categories, name='categories'),
    path('categories/<int:catid>/', categories, name='categories'),
    path('api/answer/<int:answer_id>/', answer, name='answer'),
    # path('post/<int:post_id>/', show_post, name='post'),
    # path('category/<int:cat_id>/', show_category, name='category'),

]