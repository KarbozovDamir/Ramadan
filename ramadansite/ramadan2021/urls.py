from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('api/', api),
    path('cats/<int:catid>/', categories),
]