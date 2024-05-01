
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PostView, CategoryView, CommentView

router = DefaultRouter()
# router.register(r'products', PostView, basename='product')

urlpatterns = [
    path('category/', CategoryView.as_view(), name='create_list_categories'),
    path('category/<int:category_id>/posts', PostView.as_view(), name='create_list_posts'),
    path('category/<int:category_id>/post/<int:post_id>/comments', CommentView.as_view(), name='create_list_comments'),
    # path('', include(router.urls)),
]
