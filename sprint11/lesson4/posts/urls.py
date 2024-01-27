from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
