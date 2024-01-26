from django.urls import path

from .views import APIPostDetail, APIPostList

urlpatterns = [
    path('api/v1/posts/', APIPostList.as_view()),
    path('api/v1/posts/<int:pk>/', APIPostDetail.as_view()),
]