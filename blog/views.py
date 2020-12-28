from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer



class CreatePost(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RetrieveUpdateDestroyPost(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    