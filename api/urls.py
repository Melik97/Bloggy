
from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import PostView, CategoryView, CommentView

router = DefaultRouter()

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='create_list_categories'),
    path('categories/<int:category_id>/posts/', PostView.as_view(), name='create_list_posts'),
    path('categories/<int:category_id>/posts/<int:post_id>/comments', CommentView.as_view(), name='create_list_comments'),
]
