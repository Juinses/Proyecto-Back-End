from django.contrib import admin
from django.urls import path

from Rol import views as VistasRol

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', VistasRol.seleccion_rol),
    path('<str:tipo>/', VistasRol.Tipos_rol, name='Tipos_rol'),
    path('<str:tipo>/<str:juego_nombre>/', VistasRol.descripcion_rol, name='Descripcion_rol'),
]
