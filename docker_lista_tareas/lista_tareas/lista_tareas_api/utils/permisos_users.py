from rest_framework.permissions import BasePermission, SAFE_METHODS


class SoloPuedoEditarMisTareas(BasePermission):
    """
    Define si el usuario puede editar o borrar una tarea ajena.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return (
            obj.usuario == request.user or request.user.is_superuser
        )  # si es superusuario puede editar cualquier tarea
