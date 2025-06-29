from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, AutorViewSet, EditorialViewSet, GeneroViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'editoriales', EditorialViewSet)
router.register(r'generos', GeneroViewSet)
urlpatterns = router.urls