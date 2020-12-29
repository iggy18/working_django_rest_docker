from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorized


class CreatePost(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RetrieveUpdateDestroyPost(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #ADDED TO AUTH USER
    permission_classes = [IsAuthorized]