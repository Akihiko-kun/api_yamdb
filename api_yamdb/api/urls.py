from django.urls import include, path
from rest_framework import routers

from api.views import CategoryViewSet, GenreViewSet


router = routers.DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
]
