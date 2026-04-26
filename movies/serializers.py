from rest_framework import serializers

from .models import Genre, Movie, Sala  # CAMBIO — importar Sala


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", "slug"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        source="genres",
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "release_date",
            "genres",
            "genre_ids",
            "created_at",
        ]
        read_only_fields = ["created_at"]


# NUEVO — serializer para Sala
class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ["id", "nombre", "capacidad"]