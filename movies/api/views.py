from rest_framework.generics import ListAPIView
from movies.models import Movie
from .serializers import MovieSerializer


class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_context(self):
        return {"request": self.request}
