import logfire
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.models import Category
from api.serilizers.category import CategorySerializer


class CategoryView(generics.ListCreateAPIView):
    template_name = 'category.html'
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return render(request, self.template_name, {'categories': serializer.data})

    # override delete me
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        logfire.info('Hello, {name}!', name='world')
        return redirect('categories')

