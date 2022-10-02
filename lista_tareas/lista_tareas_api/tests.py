from rest_framework.test import APITestCase

from allauth.utils import get_user_model

from django.test.client import Client

# Create your tests here.


class Login_test(APITestCase):
    def setUp(self):
        self.client = Client()
        self.username = "test@test.com"
        self.password = "password"

        nuevo_usuario = get_user_model().objects.create_user(
            username=self.username,
            password=self.password,
        )
        nuevo_usuario.save()
        self.assertEqual(nuevo_usuario.username, self.username)
        self.assertNotEqual(nuevo_usuario.password, self.password)
        self.assertTrue(nuevo_usuario.check_password(self.password))
        self.assertEqual(nuevo_usuario.is_active, True)

    def test_login(self):
        response = self.client.post(
            "/lista_tareas/v1/authentication/login/",
            {"username": self.username, "password": self.password},
        )
        self.assertEqual(response.status_code, 200)

    def test_login_falla(self):
        response = self.client.post(
            "/lista_tareas/v1/authentication/login/",
            {"username": self.username, "password": "wrong"},
        )
        self.assertEqual(response.status_code, 400)

    def test_logout(self):
        response = self.client.post(
            "/lista_tareas/v1/authentication/logout/",
            {"username": self.username, "password": self.password},
        )
        self.assertEqual(response.status_code, 200)


class crear_tarea_test(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="test"
        )
        self.user.save()
        self.client = Client()
        self.client.login(username="test", password="test")

    def test_crear_tarea(self):
        response = self.client.post(
            "/lista_tareas/v1/listado/",
            {"titulo": "test", "descripcion": "test", "completada": False},
        )
        self.assertEqual(response.status_code, 201)
