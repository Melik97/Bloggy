import logfire
from django.db import transaction
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from api.models import Category
from api.serilizers.category import CategorySerializer


class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'CREATE':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            self.permission_classes = []

        return super(CategoryView, self).get_permissions()

    @transaction.atomic
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # logfire.info('Hello, {name}!', name='world')
        return Category.objects.all()


