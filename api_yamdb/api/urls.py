from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, SignUpViewSet, TitleViewSet, UserViewSet,
                    token)

app_name = 'api'

router = SimpleRouter()
router.register('auth/signup', SignUpViewSet)
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet,
                basename='categories')
router.register('genres', GenreViewSet,
                basename='genres')
router.register('titles', TitleViewSet,
                basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', token, name='token')
]
