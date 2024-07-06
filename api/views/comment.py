from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny

from api.models import Post, Comment
from api.serilizers.comment import CommentSerializer


class CommentView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        try:
            post = Post.objects.get(id=self.kwargs.get('post_id'))
        except post.DoesNotExist:
            raise NotFound
        serializer.save(post=post)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        # return render(request, 'posts.html', {'posts': serializer.data})
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return redirect('create_list_comments', post_id=self.kwargs['post_id'], category_id=self.kwargs['category_id'])

