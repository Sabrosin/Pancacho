
# importa la funcion que permite mostrar una plantilla html
from django.shortcuts import render

# importa el modelo noticia de nuestra aplicacion
from .models import Noticia


# vista principal del portal publico de noticias
def inicio(request):

    # consulta todas las noticias registradas en la base de datos
    noticias = Noticia.objects.all()

    # envia las noticias a la plantilla html
    return render(
        request,
        'app_noticias/portal.html',
        {'noticias': noticias}
    )
