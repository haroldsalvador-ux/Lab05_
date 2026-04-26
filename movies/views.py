from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    """
    GET /api/genres/      → lista todos los géneros
    GET /api/genres/{id}/ → detalle de un género
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieViewSet(viewsets.ModelViewSet):
    """
    GET    /api/movies/      → lista películas
    POST   /api/movies/      → crea película
    GET    /api/movies/{id}/ → detalle
    PUT    /api/movies/{id}/ → actualiza
    DELETE /api/movies/{id}/ → elimina
    """

    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Movie.objects.prefetch_related("genres").all()