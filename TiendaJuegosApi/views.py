# Django
from django.http import JsonResponse
from django.contrib.auth.models import User

# Django REST Framework
from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# JWT
from rest_framework_simplejwt.tokens import RefreshToken

# Modelos
from Rol.models import Juego
from consolas.models import Consola

# Serializers
from .serializers import UserSerializer, ConsolaSerializer, JuegoSerializer

def consolasApi(request):
    if request.method == 'GET':
        consolas = Consola.objects.all()
        data = {
            'consolas': list(consolas.values(
                'nombre',
                'imagen',
                'descripcion',
                'empresa',
                'anio_salida',
                'ventas_totales',
                'juegos_vendidos'
            ))
        }
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def juegosApi(request):
    if request.method == 'GET':
        juegos = Juego.objects.all()
        data = {
            'juegos': list(juegos.values(
                'nombre',
                'imagen',
                'descripcion',
                'plataforma__nombre'
            ))
        }
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@api_view(['GET', 'POST'])
def consola_listado(request):
    if request.method == 'GET':
        consolas = Consola.objects.all()
        serializer = ConsolaSerializer(consolas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ConsolaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def consola_detalle(request, pk):
    try:
        consola = Consola.objects.get(id=pk)
    except Consola.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConsolaSerializer(consola)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConsolaSerializer(consola, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        consola.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def juego_listado(request):
    if request.method == 'GET':
        juegos = Juego.objects.all()
        serializer = JuegoSerializer(juegos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = JuegoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def juego_detalle(request, pk):
    try:
        juego = Juego.objects.get(id=pk)
    except Juego.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JuegoSerializer(juego)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JuegoSerializer(juego, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        juego.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ConsolaViewSet(viewsets.ModelViewSet):
    queryset = Consola.objects.all()
    serializer_class = ConsolaSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class JuegoViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden cerrar sesión

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout exitoso"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "Token inválido o faltante"}, status=status.HTTP_400_BAD_REQUEST)