from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    # Declarar el campo explícitamente asegura que DRF gestione la URL completa
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Movie
        # Listar los campos explícitamente es una buena práctica para el control de datos
        fields = [
            'id', 
            'title', 
            'description', 
            'image', 
            'release_date', 
            'created_at', 
            'updated_at'
        ]