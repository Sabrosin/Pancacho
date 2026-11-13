
# importa las herramientas para configurar las rutas
from django.contrib import admin
from django.urls import path, include

# importa las configuraciones de django
from django.conf import settings

# importa la herramienta para gestionar archivos multimedia
from django.conf.urls.static import static


# lista de rutas principales del proyecto
urlpatterns = [

    # ruta para acceder al panel administrativo de django
    path('admin/', admin.site.urls),

    # conecta las rutas de nuestra aplicacion de noticias
    path('', include('app_noticias.urls')),

]


# permite mostrar imagenes durante el desarrollo
if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
