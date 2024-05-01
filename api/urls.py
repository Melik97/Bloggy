
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PostView, CategoryView

router = DefaultRouter()
# router.register(r'products', PostView, basename='product')

urlpatterns = [
    path('post/', PostView.as_view()),
    path('category/', CategoryView.as_view(), name='categories'),
    # path('', include(router.urls)),
]
