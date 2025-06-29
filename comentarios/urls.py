from rest_framework.routers import DefaultRouter
from .views import ComentarioViewSet, CalificacionViewSet

router = DefaultRouter()
router.register(r'comentarios', ComentarioViewSet)
router.register(r'calificaciones', CalificacionViewSet)
urlpatterns = router.urls