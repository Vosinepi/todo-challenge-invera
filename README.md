# API Lista de tareas

Pequeña api para crear, listar, editar y eliminar tareas.

## Documentacion consultada

Libreria API REST

- [Django Rest Framework](https://www.django-rest-framework.org/)

Libreria para autenticacion por token

- [Django Rest Auth](https://dj-rest-auth.readthedocs.io/en/latest/)

Libreria para crear usuarios

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html)

## pasos previos antes de su utilizacion

1. Clonar este repositorio

`git clone https://github.com/Vosinepi/todo-challenge-invera`

2. Ejecutar conteiner de docker

`docker-compose up`

3. Ejecutar entorno virtual

`source venv/bin/activate`

4. Instalar dependencias

`pip install -r requirements.txt`

5. Ejecutar migraciones

`python manage.py migrate`

6. Crear super usuario

`python manage.py createsuperuser`

username: admin
email: admin@amdmin.com
password: admin

7. Ejecutar servidor

`python manage.py runserver`

### Para acceder a la api hay que ingresar las credenciales

- login
  `http://127.0.0.1:8000/lista_tareas/authentication/login`
- logout
  `http://127.0.0.1:8000/lista_tareas/authentication/logout`
- user
  `http://127.0.0.1:8000/lista_tareas/authentication/user`
- registro
  `http://127.0.0.1:8000/lista_tareas/registration/`

## ENDPOINTS

Listado de tareas

`http://127.0.0.1:8000/lista_tareas/listado/`

Crear tarea POST

`http://127.0.0.1:8000/lista_tareas/listado/`

Ver tarea

`http://127.0.0.1:8000/lista_tareas/tarea/<pk>/`

Editar tarea PUT

`http://127.0.0.1:8000/lista_tareas/tarea/<pk>/`

Eliminar tarea DELETE

`http://127.0.0.1:8000/lista_tareas/tarea/<pk>/`

Actualizar estado de tarea

`http://127.0.0.1:8000/lista_tareas/tarea/<pk>/`

### Buscar tareas FILTER

`http://127.0.0.1:8000/lista_tareas/buscar/?search=`

## Documentacion consultada

Libreria API REST

- [Django Rest Framework](https://www.django-rest-framework.org/)

Libreria para autenticacion por token

- [Django Rest Auth](https://dj-rest-auth.readthedocs.io/en/latest/)

Libreria para crear usuarios

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html)
