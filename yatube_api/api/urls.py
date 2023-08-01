from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import CommentViewSet, PostViewSet, GroupViewSet


router = DefaultRouter()

router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')
router.register('groups', GroupViewSet, basename='group')
router.register('posts', PostViewSet, basename='post')


urlpatterns = [
    path('v1/', include(router.urls)),
]
