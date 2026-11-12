
# importa las herramientas para personalizar el panel administrativo
from django.contrib import admin

# importa el modelo Noticia de nuestra aplicacion
from .models import Noticia


# clase encargada de personalizar la administracion de las noticias
class NoticiaAdmin(admin.ModelAdmin):

    # columnas que apareceran en el listado de noticias
    list_display = ('titulo', 'fecha_ocurrencia', 'lugar')

    # filtros disponibles para organizar las noticias
    list_filter = ('fecha_ocurrencia', 'lugar')

    # campos que utilizaremos para buscar noticias
    search_fields = ('titulo', 'lugar', 'descripcion')

    # ordena las noticias desde la mas reciente
    ordering = ('-fecha_ocurrencia',)

    # campos que apareceran en el formulario de edicion
    fields = ('titulo', 'fecha_ocurrencia', 'lugar', 'descripcion', 'imagen')


# registra el modelo y su configuracion en el panel administrativo
admin.site.register(Noticia, NoticiaAdmin)
