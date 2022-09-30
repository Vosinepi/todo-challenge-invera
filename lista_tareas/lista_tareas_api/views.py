from django.shortcuts import render
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

# modelo
from .models import Tareas

# serializador
from .serializer import TareasSerializer


# Create your views here.


class Tareas_listado_api(generics.ListCreateAPIView):
    """
    ENDPOINT para la lista de tareas.
    """

    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer
    permission_classes = [permissions.IsAuthenticated]


# class Tareas_listado_api(APIView):
#     """
#     ENDPOINT para la lista de tareas.
#     """

#     # permisos
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         """
#         Devuelve todas las tareas del usuario.
#         """
#         tareas = Tareas.objects.filter(usuario=request.user)
#         serializer = TareasSerializer(tareas, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, *args, **kwargs):
#         """
#         Crea una tarea para el usuario.
#         """
#         datos = {
#             "titulo": request.data.get("titulo"),
#             "descripcion": request.data.get("descripcion"),
#             "completada": request.data.get("completada"),
#             "usuario": request.user.id,
#         }

#         serializer = TareasSerializer(data=datos)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Tarea_detalle_api(generics.RetrieveUpdateDestroyAPIView):
    """
    ENDPOINT para tarea que permite BORRAR, EDITAR o cambiar el ESTADO.
    """

    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer
    permission_classes = [permissions.IsAuthenticated]


# class Tarea_detalle_api(APIView):
#     """
#     ENDPOINT para tarea que permite BORRAR y EDITAR.
#     """

#     # permisos
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, pk):
#         """
#         Devuelve una tarea del usuario.
#         """
#         tarea = Tareas.objects.get(id=pk)
#         serializer = TareasSerializer(tarea)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk, *args, **kwargs):
#         """
#         Actualiza una tarea para el usuario.
#         """
#         tarea = Tareas.objects.get(id=pk)
#         if not tarea:
#             return Response(
#                 {"res": "Tarea con ese ID no existe"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         datos = {
#             "titulo": request.data.get("titulo"),
#             "descripcion": request.data.get("descripcion"),
#             "completada": request.data.get("completada"),
#             "usuario": request.user.id,
#         }

#         serializer = TareasSerializer(instance=tarea, data=datos, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, *args, **kwargs):
#         """
#         Elimina una tarea para el usuario.
#         """
#         tarea = Tareas.objects.get(id=pk)
#         tarea.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class Buscar_tarea_api(generics.ListAPIView):
    """
    ENDPOINT para buscar tareas por titulo.
    """

    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["descripcion", "fecha_creacion"]
