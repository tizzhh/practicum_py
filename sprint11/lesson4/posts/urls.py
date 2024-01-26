from django.urls import path

from .views import api_posts, api_posts_detail

urlpatterns = [
    path('api/v1/posts/', api_posts),
    path('api/v1/posts/<int:pk>/', api_posts_detail),
]
