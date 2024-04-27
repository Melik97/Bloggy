from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer

from api.models import Post
from api.serilizers import PostSerializer
from bloggy import settings


class PostView(generics.ListCreateAPIView):
    template_name = 'Index.html'
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # This method is used for GET requests
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return render(request, self.template_name, {'data': serializer.data})

    # override delete me
    def post(self, request, *args, **kwargs):
        created = self.create(request, *args, **kwargs)
        return created
