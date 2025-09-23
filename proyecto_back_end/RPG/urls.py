from django.contrib import admin
from django.urls import path
from Rol import views as VistasRol
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home: listar géneros
    path('', VistasRol.home, name='home'),

    # Listado de juegos por género
    path('genero/<int:genero_id>/', VistasRol.juegos_por_genero, name='juegos_por_genero'),

    # Detalle del juego
    path('juego/<int:juego_id>/', VistasRol.descripcion_rol, name='descripcion_rol'),

    # Crear y editar juegos
    path('juego/crear/', VistasRol.manejar_juego, name='crear_juego'),
    path('juego/editar/<int:pk>/', VistasRol.manejar_juego, name='editar_juego'),

    # Eliminar juego
    path('juego/eliminar/<int:pk>/', VistasRol.eliminar_juego, name='eliminar_juego'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
