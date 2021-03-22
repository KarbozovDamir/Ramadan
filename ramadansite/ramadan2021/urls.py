from django.urls import path

from .views import *


urlpatterns = [
    path('', index),
    path('api/categories/', api),
    path('api/categories/<int:catid>/', categories),

]