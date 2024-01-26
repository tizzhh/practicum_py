from django.http import JsonResponse

from .models import Post
from .serializers import PostSerializer


def get_post(request, pk):
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)
