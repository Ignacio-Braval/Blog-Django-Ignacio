from rest_framework.permissions import BasePermission
from comments.models import Comment


'''
*Esta clase fue implementada para que el dueño tenga todos los permisos o
 solo puede leer los comentarios y crearlos, nada mas.

*Si la petición es de tipo get o post todo el mundo tiene los permisos,
 en el caso contrario estaria actualizando o intentando eliminar,
 por eso sacamos el id del comentario que esta intentando actualizar o eliminar.

*despues hacemos una petición a la BD para obtener los datos de ese comentario.

*luego seguimos sacando el id del usuario que ejecutando la petición.

*luego obtenemos el id del usuario que hemos obtenido.

*comparamos diciendo si el id del usuario que esta haciendo la petición es el mismo
 del usuario que creo el comentario, entonces podra eliminarlo o actualizarlo, de lo
 contrario no tendra los permisos para esas acciones.
'''


class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk']
            comment = Comment.objects.get(pk=id_comment)

            id_user = request.user.pk
            id_user_comment = comment.user_id

            if id_user == id_user_comment:
                return True

            return False
