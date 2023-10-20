from django.urls import path

from . import views

urlpatterns = [
    # Напишите адрес тут
    path('', views.index),
]