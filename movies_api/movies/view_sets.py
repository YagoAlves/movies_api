from rest_framework.viewsets import ModelViewSet
from .serializers import MoviesSerializer
from .models import Movies
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class MoviesViewSet(ModelViewSet):

    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["date_published", "reviews", "votes"]
    search_fields = ["imdb_id", "title", "genre", "duration", "country", "language", "date_published"]
