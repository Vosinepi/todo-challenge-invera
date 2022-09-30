from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from .models import *

# Create your tests here.


class test_tareas(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_listado_tareas(self):
        """
        Comprobamos que el listado de tareas devuelve un 200.
        """
        url = reverse("lista_tareas_api:listado")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_tarea(self):
        """
        Comprobamos que al crear una tarea devuelve un 201.
        """
        url = reverse("lista_tareas_api:listado")
        data = {"titulo": "test", "descripcion": "test"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class userTestCase(APITestCase):
#     def test_user(self):
#         """
#         Test creacion usuario
#         """
#         url = "/registration/"
#         data = {
#             "username": "test",
#             "email": "test",
#             "password1": "test",
#             "password2": "test",
#         }


# class tareaTestCase(APITestCase):
#     def test_tarea(self):
#         """
#         Test creacion tarea
#         """
#         url = "/listado/"
#         data = {
#             "titulo": "test",
#             "descripcion": "test",
#             "completada": "test",
#         }


# class buscarTareaTestCase(APITestCase):
#     def test_buscar_tarea(self):
#         """
#         Test buscar tarea
#         """
#         url = "/buscar/"
#         data = {
#             "descripcion": "test",
#         }


# class tareaDetalleTestCase(APITestCase):
#     def test_tarea_detalle(self):
#         """
#         Test tarea detalle
#         """
#         url = "/tarea/1/"
#         data = {
#             "titulo": "test",
#             "descripcion": "test",
#             "completada": "test",
#         }


# class test_tarea_authorization(APITestCase):
#     def test_tarea_authorization(self):
#         """
#         Test tarea authorization
#         """
#         url = "/authentication/"
#         data = {
#             "username": "test",
#             "password": "test",
#         }
