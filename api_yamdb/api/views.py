from rest_framework import permissions
# from api.permissions import IsAuthorOrReadOnly
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from rest_framework import viewsets
from .serializers import (
    UserSerializer,
    CategorySerializer,
    GenreSerializer,
    TitleSerializer
)
from reviews.models import User, Category, Genre, Title


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Viewset для модели Category."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
#    permission_classes = [IsAuthenticatedOrReadOnly]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
#    permission_classes = [IsAuthenticatedOrReadOnly]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    