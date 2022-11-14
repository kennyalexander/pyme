from django.db import models

# Create your models here.
class Productos(models.Model):
  nombre = models.CharField(max_length=30)
  descripcion = models.TextField()
  disponible = models.BooleanField()
  fechaIncorporacion = models.DateField()
  nombrePyme = models.CharField(max_length=30)
  urlimage = models.CharField(max_length=100)

