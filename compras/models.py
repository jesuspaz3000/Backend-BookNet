from django.db import models
from usuarios.models import Usuario
from libros.models import Libro

# Create your models here.
class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField(default=1)
