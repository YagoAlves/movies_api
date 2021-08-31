from .models import Movies


class Mocks():

    def create_movies(self):

        Movies.objects.bulk_create(
            [
                Movies(imdb_id="tt8764144", title="A Wakefield Project", original_title="A Wakefield Project",
                               year="2019", genre="Horror, Sci-Fi, Thriller", duration="88",
                               country="Canada, USA", language="English", votes=266,
                               budget="$500.000", reviews=12.0, date_published="2021-05-07"),
                
                Movies(imdb_id="tt8637440", title="The Climb", original_title="The Climb",
                               year="2019", genre="Comedy, Drama", duration="94",
                               country="USA", language="English", votes=567,
                               budget="$1000.000", reviews=2.0, date_published="2020-11-13"),
                
                Movies(imdb_id="tt10749786", title="Atlantis", original_title="Atlantis",
                               year="2019", genre="Drama", duration="106",
                               country="Ukraine", language="Ukrainian, English", votes=296,
                               budget="$2000.000", reviews=15.0, date_published="2020-11-05"),

                Movies(imdb_id="tt9048786", title="L'immortale", original_title="L'immortale",
                               year="2019", genre="Crime, Drama", duration="116",
                               country="Italy, Germany", language="Italian, Latvian, Neapolitan", votes=2507,
                               budget="$200.000", reviews=27.0, date_published="2019-12-05"),

                Movies(imdb_id="tt9055630", title="H0us3", original_title="H0us3",
                               year="2018", genre="Horror, Sci-Fi, Thriller", duration="105",
                               country="Spain", language="Spanish", votes=436,
                               budget="$700.000", reviews=7.0, date_published="2021-06-05"),

            ]
        )
        id_movies = Movies.objects.values("id").first()
        return id_movies
