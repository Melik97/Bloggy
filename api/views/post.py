from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.models import Post
from api.serilizers import PostSerializer


class PostView(generics.ListCreateAPIView):
    template_name = 'Index.html'
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return render(request, self.template_name, {'data': serializer.data})

    def post(self, request, *args, **kwargs):
        print(request, *args, **kwargs)
        created = self.create(request, *args, **kwargs)
        return created
