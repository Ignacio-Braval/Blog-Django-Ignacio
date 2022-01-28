from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    # La siguiente linea solo entregara las categorias que se encuentran publicadas
    queryset = Category.objects.filter(published=True)
    # Con la siguiente linea podemos cambiar que la busqueda de Id pase
    # a requerir el slug de la categoria
    lookup_field = 'slug'
    # Las siguientes lineas indican que tipos de filtros se usaran (published)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
