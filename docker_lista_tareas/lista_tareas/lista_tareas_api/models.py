from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tareas(models.Model):
    """
    Creamos un modelo de tareas con los siguientes campos:
    - titulo
    - descripcion
    - fecha_creacion
    - estado de la tarea
    - usuario que la crea
    """

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
