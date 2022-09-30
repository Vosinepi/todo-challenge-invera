from rest_framework.test import APITestCase


# Create your tests here.


class userTestCase(APITestCase):
    def test_user(self):
        """
        Test creacion usuario
        """
        url = "/registration/"
        data = {
            "username": "test",
            "email": "test",
            "password1": "test",
            "password2": "test",
        }


class tareaTestCase(APITestCase):
    def test_tarea(self):
        """
        Test creacion tarea
        """
        url = "/listado/"
        data = {
            "titulo": "test",
            "descripcion": "test",
            "completada": "test",
        }


class buscarTareaTestCase(APITestCase):
    def test_buscar_tarea(self):
        """
        Test buscar tarea
        """
        url = "/buscar/"
        data = {
            "descripcion": "test",
        }


class tareaDetalleTestCase(APITestCase):
    def test_tarea_detalle(self):
        """
        Test tarea detalle
        """
        url = "/tarea/1/"
        data = {
            "titulo": "test",
            "descripcion": "test",
            "completada": "test",
        }
