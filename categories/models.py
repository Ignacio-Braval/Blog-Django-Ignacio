from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    # slug es la url de nuestra categoria
    slug = models.SlugField(max_length=255, unique=True)
    # Esta linea indica que las categorias por default estran despublicadas
    published = models.BooleanField(default=False)

    # Esta linea es para que el futuro cuando creemos un post y se nos abra
    # un desplegable se muestre un dato de la categoria
    def __str__(self):
        return self.title
