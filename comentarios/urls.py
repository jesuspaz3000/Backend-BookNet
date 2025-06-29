from rest_framework.routers import DefaultRouter
from .views import ComentarioViewSet, CalificacionViewSet

router = DefaultRouter()
router.register(r'comentarios', ComentarioViewSet, basename='comentario')
router.register(r'calificaciones', CalificacionViewSet, basename='calificacion')
urlpatterns = router.urls