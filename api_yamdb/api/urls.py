from django.urls import include, path
from rest_framework import routers
from api.views import CategoryViewSet, GenreViewSet, TitleViewSet, ReviewViewSet, CommentViewSet, UserViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<reviews_id>\d+)/comments', CommentViewSet, basename='reviews'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
