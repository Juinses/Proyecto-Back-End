from django.contrib import admin
from django.urls import path
from Rol import views as VistasRol
from consolas import views as VistasConsolas
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #ruta pagina principal
    path('', VistasRol.home, name='home'),

    #rutas juegos
    # Home: listar géneros
    path('juegos/', VistasRol.home_juegos, name='home_juegos'),

    # Listado de juegos por género
    path('genero/<int:genero_id>/', VistasRol.juegos_por_genero, name='juegos_por_genero'),

    # Detalle del juego
    path('juego/<int:juego_id>/', VistasRol.descripcion_rol, name='descripcion_rol'),

    # Crear y editar juegos
    path('juego/crear/', VistasRol.manejar_juego, name='crear_juego'),
    path('juego/editar/<int:pk>/', VistasRol.manejar_juego, name='editar_juego'),

    # Eliminar juego
    path('juego/eliminar/<int:pk>/', VistasRol.eliminar_juego, name='eliminar_juego'),


    #rutas empresa
    # Home: listar empresas
    path('empresas/', VistasConsolas.home_empresas, name='home_empresas'),

    # Listado de consolas por empresa
    path('empresa/<int:empresa_id>/', VistasConsolas.consolas_por_empresa, name='consolas_por_empresa'),

    # Detalle de la consola
    path('consola/<int:consola_id>/', VistasConsolas.descripcion_consola, name='descripcion_consola'),

    # Crear y editar consolas
    path('consola/crear/', VistasConsolas.manejar_consola, name='crear_consola'),
    path('consola/editar/<int:pk>/', VistasConsolas.manejar_consola, name='editar_consola'),

    # Eliminar consolas
    path('consola/eliminar/<int:pk>/', VistasConsolas.eliminar_consola, name='eliminar_consola'),

    # Lista de empresas
    path('empresas/', VistasConsolas.lista_empresas, name='lista_empresas'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
