from rest_framework import viewsets
from .models import Comentario, Calificacion
from .serializers import ComentarioSerializer, CalificacionSerializer

# Create your views here.
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    
class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer