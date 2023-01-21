from django.urls import include, path
from rest_framework import routers
from api.views import CategoryViewSet, GenreViewSet, TitleViewSet   

app_name = 'api'

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
