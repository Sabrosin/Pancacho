

# importa las herramientas necesarias para crear modelos
from django.db import models


# modelo encargado de almacenar las noticias del centro
class Noticia(models.Model):

    # titulo de la noticia
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título de la noticia'
    )

    # fecha en la que ocurrio el acontecimiento
    fecha_ocurrencia = models.DateField(
        verbose_name='Fecha de ocurrencia'
    )

    # lugar donde ocurrio la noticia
    lugar = models.CharField(
        max_length=150,
        verbose_name='Lugar'
    )

    # descripcion completa de la noticia
    descripcion = models.TextField(
        verbose_name='Descripción'
    )

    # imagen relacionada con la noticia
    imagen = models.ImageField(
        upload_to='noticias/',
        verbose_name='Imagen de la noticia'
    )

    # representa cada noticia utilizando su titulo
    def __str__(self):
        return self.titulo

    # configuraciones generales del modelo
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ['-fecha_ocurrencia']
