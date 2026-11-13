
# importa la herramienta para definir las rutas
from django.urls import path

# importa las vistas de nuestra aplicacion
from . import views


# define las rutas disponibles de la aplicacion
urlpatterns = [

    # ruta principal del portal publico de noticias
    path('', views.inicio, name='inicio'),

]
