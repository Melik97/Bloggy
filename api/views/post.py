from django.db import transaction
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from api.models import Post, Category
from api.serilizers import PostSerializer


class PostView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        try:
            category = Category.objects.get(id=self.kwargs.get('category_id'))
        except category.DoesNotExist:
            raise NotFound
        serializer.save(category=category)

    def get_permissions(self):
        if self.request.method == 'CREATE':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            self.permission_classes = []

        return super(PostView, self).get_permissions()

    @transaction.atomic
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # logfire.info('Hello, {name}!', name='world')
        return Post.objects.all()

