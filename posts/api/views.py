from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    # La siguiente linea filtra los post por el id de la categoria
    # colocando ['category'], ahora si queremos filtar por el slug u
    # otro atributo, debe ser asi: ['category__slug']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__slug']
    # filterset_fields = ['category']
