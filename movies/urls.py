from rest_framework.routers import DefaultRouter

from .views import GenreViewSet, MovieViewSet, SalaViewSet  # CAMBIO

router = DefaultRouter()
router.register(r"genres", GenreViewSet, basename="genre")
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"salas", SalaViewSet, basename="sala")  # NUEVO

urlpatterns = router.urls