from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from reviews.models import Category, Genre
from api.serializers import (
    CategorySerializer,
    GenreSerializer
)


class CreateListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    Набор представлений, обеспечивающий действия `create` и `list`.
    """

    pass


class CategoryViewSet(viewsets.ModelViewSet):
    """Viewset для модели Category."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

#    queryset = Post.objects.all()
#    serializer_class = PostSerializer
#    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
#    pagination_class = LimitOffsetPagination

#
#     def perform_create(self, serializer):
#        """Переопределяем сохранение автора."""
#        serializer.save(author=self.request.user)