from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    email= models.EmailField(unique=True)