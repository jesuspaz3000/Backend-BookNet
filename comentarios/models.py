from django.db import models
from usuarios.models import Usuario
from libros.models import Libro


# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Calificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    calificacion = models.IntegerField()  # Asumiendo que la calificación es un número entero
    fecha_creacion = models.DateTimeField(auto_now_add=True)
