# posts/urls.py
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

from .views import PostDetail, PostList

urlpatterns = [
    path('api/v1/posts/', PostList.as_view()),
    path('api/v1/posts/<int:pk>/', PostDetail.as_view()),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
