from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import CommentViewSet, PostViewSet, GroupViewSet


router = DefaultRouter()

router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')
router.register(r'v1/groups', GroupViewSet, basename='group')
router.register(r'v1/posts', PostViewSet, basename='post')


urlpatterns = [
    path('', include(router.urls)),
]
