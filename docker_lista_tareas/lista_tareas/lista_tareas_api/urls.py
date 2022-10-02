from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

# vistas
from .views import Tareas_listado_api, Tarea_detalle_api, Buscar_tarea_api

app_name = "lista_tareas_api"

urlpatterns = [
    path("listado/", Tareas_listado_api.as_view(), name="listado"),
    path("tarea/<int:pk>/", Tarea_detalle_api.as_view()),
    path("buscar/", Buscar_tarea_api.as_view()),
    path("authentication/", include("dj_rest_auth.urls")),  # urls de autenticación
    path(
        "registration/", include("dj_rest_auth.registration.urls")
    ),  # urls de registro
    path("token/", obtain_auth_token, name="api_token_auth"),  # token
]
