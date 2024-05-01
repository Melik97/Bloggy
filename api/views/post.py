from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny

from api.models import Post, Category
from api.serilizers import PostSerializer


class PostView(generics.ListCreateAPIView):
    template_name = 'posts.html'
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        try:
            category = Category.objects.get(id=self.kwargs.get('category_id'))
        except category.DoesNotExist:
            raise NotFound
        serializer.save(category=category)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return render(request, self.template_name, {'posts': serializer.data})

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return redirect('create_list_posts', category_id=self.kwargs['category_id'])

