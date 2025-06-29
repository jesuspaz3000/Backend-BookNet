from django.urls import path
from .views import recomendaciones_view

urlpatterns = [
    path('api/recomendaciones/<int:user_id>/', recomendaciones_view),
]