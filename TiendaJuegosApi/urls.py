from rest_framework.routers import DefaultRouter
from .views import ConsolaViewSet, JuegoViewSet

router = DefaultRouter()
router.register(r'consolas', ConsolaViewSet, basename='consolas')
router.register(r'juegos', JuegoViewSet, basename='juegos')

urlpatterns = router.urls
