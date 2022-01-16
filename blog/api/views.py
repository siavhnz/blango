from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.models import Post
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from rest_framework.permissions import IsAdminUser

class PostList(generics.ListCreateAPIView):
    #authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer