from django.core.management.base import BaseCommand
from movies.models import Movies
from datetime import datetime
import csv


IMDB_ID = 0
TITLE = 1
ORIGINAL_TITLE = 2
YEAR = 3
DATE_PUBLISHED = 4
GENRE = 5
DURATION = 6
COUNTRY = 7
LANGUAGE = 8
DIRECTOR = 9
VOTES = 15
BUDGET = 16
REVIEWS = 20


class Command(BaseCommand):

    help = "Load the movies csv file"

    def handle(self, *args, **kwargs):

        insert_list = []

        Movies.objects.all().delete()

        with open("/home/yago/Documentos/movies_api/movies_api/movies/management/commands/IMDb movies.csv") as csv_file:
            
            csv_reader = csv.reader(csv_file, delimiter=',')
            count = 0
            for row in csv_reader:
                if count != 0:
                    movies = Movies()
                    movies.imdb_id = row[IMDB_ID]
                    movies.title = row[TITLE]
                    movies.original_title = row[ORIGINAL_TITLE]
                    movies.year = row[YEAR]
                    try:
                        movies.date_published = datetime.strptime(row[DATE_PUBLISHED], '%Y-%m-%d')
                    except ValueError:
                        print("Not able to convert")
                    movies.genre = row[GENRE]
                    movies.duration = row[DURATION]
                    movies.country = row[COUNTRY]
                    movies.language = row[LANGUAGE]
                    movies.votes = row[VOTES]
                    movies.budget = row[BUDGET]
                    if row[REVIEWS]:
                        movies.reviews = row[REVIEWS]
                    
                    insert_list.append(movies)
                count += 1
        Movies.objects.bulk_create(insert_list, batch_size=500)