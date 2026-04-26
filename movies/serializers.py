from rest_framework import serializers

from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    """Serializer para Genre."""

    class Meta:
        model = Genre
        fields = ["id", "name", "slug"]


class MovieSerializer(serializers.ModelSerializer):
    """Serializer para Movie."""

    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "release_date",
            "genres",
            "created_at",
        ]