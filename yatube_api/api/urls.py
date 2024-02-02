from django.urls import path, include, path
from rest_framework import routers
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


api_v1_router = routers.DefaultRouter()
api_v1_router.register(r'posts', PostViewSet, basename='posts')
api_v1_router.register(r'groups', GroupViewSet, basename='groups')
api_v1_router.register(r'follow', FollowViewSet, basename='follow')
api_v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('v1/', include(api_v1_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
