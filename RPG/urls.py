from django.contrib import admin
from django.urls import path
from Rol import views as VistasRol
from consolas import views as VistasConsolas
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from TiendaJuegosApi import views as rol_views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)


urlpatterns = [
    path('admin/', admin.site.urls),
    # Login y logout
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # ruta página principal
    path('', VistasRol.home, name='home'),

    # rutas juegos
    path('juegos/', VistasRol.home_juegos, name='home_juegos'),
    path('plataforma/<int:plataforma_id>/', VistasRol.juegos_por_plataforma, name='juegos_por_plataforma'),
    path('juego/<int:juego_id>/', VistasRol.descripcion_rol, name='descripcion_rol'),
    path('plataforma/<int:plataforma_id>/juego/crear/', VistasRol.manejar_juego, name='crear_juego'),
    path('juego/editar/<int:pk>/', VistasRol.manejar_juego, name='editar_juego'),
    path('juego/eliminar/<int:pk>/', VistasRol.eliminar_juego, name='eliminar_juego'),

    # rutas empresas
    path('empresas/', VistasConsolas.home_companies, name='home_empresas'),
    path('empresas/lista/', VistasConsolas.lista_companies, name='lista_empresas'),
    path('empresa/<int:company_id>/', VistasConsolas.consolas_por_company, name='consolas_por_company'),
    path('consola/<int:consola_id>/', VistasConsolas.descripcion_consola, name='descripcion_consola'),
    path('empresa/<int:company_id>/consola/crear/', VistasConsolas.manejar_consola, name='crear_consola'),
    path('consola/editar/<int:pk>/empresa/<int:company_id>/', VistasConsolas.manejar_consola, name='editar_consola'),
    path('consola/eliminar/<int:pk>/', VistasConsolas.eliminar_consola, name='eliminar_consola'),

    # Rutas API
    path('api/consolas/', rol_views.consolasApi, name='api_consolas'),
    path('api/juegos/', rol_views.juegosApi, name='api_juegos'),

    # Consolas
    path('api/consolas/', rol_views.consola_listado, name='consola_listado'),
    path('api/consolas/<int:pk>/', rol_views.consola_detalle, name='consola_detalle'),

    # Juegos
    path('api/juegos/', rol_views.juego_listado, name='juego_listado'),
    path('api/juegos/<int:pk>/', rol_views.juego_detalle, name='juego_detalle'),

    # JWT Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)