from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from Rol.models import Juego
from consolas.models import Consola
from .serializers import JuegoSerializer, ConsolaSerializer
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