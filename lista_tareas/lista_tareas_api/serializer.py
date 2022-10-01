# rest_framework
from rest_framework import serializers

# modelo
from .models import Tareas


class TareasSerializer(serializers.ModelSerializer):
    """
    Convertimos el modelo de tareas en un formato API como JSON.
    Rest Framework utiliza la clase ModelSerializer para convertir modelos.
    """

    class Meta:
        model = Tareas
        fields = "__all__"
