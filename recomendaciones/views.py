from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import obtener_recomendaciones

@api_view(['GET'])
# Create your views here.
def recomendaciones_view(request, user_id):
    data = obtener_recomendaciones(user_id)
    return Response({'recomendaciones':data})