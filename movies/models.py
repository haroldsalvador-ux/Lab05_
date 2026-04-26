from django.db import models


class Genre(models.Model):
    """Género cinematográfico. Ej: Acción, Drama, Comedia."""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Género"
        verbose_name_plural = "Géneros"

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    """Película disponible en el cine."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    release_date = models.DateField()
    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title 
      

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre