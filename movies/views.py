from rest_framework import viewsets, permissions, filters

from .models import Genre, Movie, Sala  # CAMBIO — importar Sala
from .serializers import GenreSerializer, MovieSerializer, SalaSerializer  # CAMBIO


class GenreViewSet(viewsets.ModelViewSet):
    """CRUD de géneros cinematográficos."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"


class MovieViewSet(viewsets.ModelViewSet):
    """CRUD de películas."""

    queryset = Movie.objects.prefetch_related("genres").all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "genres__name"]
    ordering_fields = ["title", "release_date", "duration"]
    ordering = ["-release_date"]


# NUEVO — ViewSet para Sala
# CAMBIO — solo para desarrollo/pruebas
class SalaViewSet(viewsets.ModelViewSet):
    """CRUD de salas del cine."""

    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [permissions.AllowAny]  # CAMBIO temporal