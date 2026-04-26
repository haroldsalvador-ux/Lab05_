from django.contrib import admin

from .models import Genre, Movie, Sala


# NUEVO — registro de Genre
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    search_fields = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}  # IMPORTANTE: autogenera el slug


# NUEVO — registro de Movie
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "duration", "release_date"]
    search_fields = ["title"]
    filter_horizontal = ["genres"]  # IMPORTANTE: widget cómodo para ManyToMany


# NUEVO — registro de Sala
@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "capacidad"]
    search_fields = ["nombre"]