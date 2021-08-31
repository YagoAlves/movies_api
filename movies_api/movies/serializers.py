from rest_framework.serializers import ModelSerializer
from .models import Movies


class MoviesSerializer(ModelSerializer):

    class Meta:
        model = Movies
        fields = ("id", "imdb_id", "title", "original_title", "year", 
                        "genre", "duration", "country", "language",
                        "votes", "budget", "reviews", "date_published")
