from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    # La sgt linea crea el campo miniature que podra cargar imagenes, y a su vez
    # se creara una carpeta llamada images dentro de la carpeta de la app posts
    miniature = models.ImageField(upload_to='posts/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    # La sgt linea crea el campo user y category que a su vez es una foreignkey
    # y cuando el usuario sea eliminado el post y la categoria seguiran visible
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title
