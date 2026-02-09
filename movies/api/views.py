from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from movies.models import Movie
from movies.serializers import MovieSerializer
from django.shortcuts import get_object_or_404

# -------------------------
# Vistas públicas
# -------------------------

@api_view(["GET"])
def movie_list(request):
    """Listado de todas las películas (público)"""
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def movie_detail(request, pk):
    """Detalle de una película por ID (público)"""
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# -------------------------
# Vistas protegidas (solo usuarios autenticados)
# -------------------------

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def movie_create(request):
    """Crear una nueva película"""
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def movie_edit(request, pk):
    """Editar una película existente"""
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def movie_delete(request, pk):
    """Eliminar una película"""
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
