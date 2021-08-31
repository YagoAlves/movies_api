from django.test import TestCase
from django.test import Client
from .mocks import Mocks
from rest_framework import status

MOVIES_SET_URL = "/movies/"


class MoviesTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.mocks = Mocks()

    def test_regular_get(self):
        
        """
        After creating the movies, there should be 5 movies.
        """

        # WHEN
        self.mocks.create_movies()
        
        # THEN
        response = self.client.get(MOVIES_SET_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 5)

    def test_get_search_imdb_id(self):
        
        """
        imdb_id tt8764144 is a known movie from the mockup file.
        """
        # GIVEN
        self.mocks.create_movies()
        
        # WHEN           
        response = self.client.get(MOVIES_SET_URL + "?search=tt8764144")
        
        # THEN
        data = response.data
        expected_data = data["results"][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 1)
        self.assertEqual(expected_data["imdb_id"], "tt8764144")
        self.assertEqual(expected_data["title"], "A Wakefield Project")
        self.assertEqual(expected_data["original_title"], "A Wakefield Project")
        self.assertEqual(expected_data["year"], "2019")
        self.assertEqual(expected_data["genre"], "Horror, Sci-Fi, Thriller")
        self.assertEqual(expected_data["duration"], "88")
        self.assertEqual(expected_data["country"], "Canada, USA")
        self.assertEqual(expected_data["language"], "English")
        self.assertEqual(expected_data["votes"], 266)
        self.assertEqual(expected_data["budget"], "$500.000")
        self.assertEqual(expected_data["reviews"], 12.0)
        self.assertEqual(expected_data["date_published"], "2021-05-07")

    def test_get_search_language(self):
        
        """
        language Ukraine is a known movie from the mockup file.
        """

        # GIVEN
        self.mocks.create_movies()
        
        # WHEN
        response = self.client.get(MOVIES_SET_URL + "?search=Ukraine")
        
        # THEN
        data = response.data
        expected_data = data["results"][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 1)
        self.assertEqual(expected_data["imdb_id"], "tt10749786")
        self.assertEqual(expected_data["title"], "Atlantis")
        self.assertEqual(expected_data["original_title"], "Atlantis")
        self.assertEqual(expected_data["year"], "2019")
        self.assertEqual(expected_data["genre"], "Drama")
        self.assertEqual(expected_data["duration"], "106")
        self.assertEqual(expected_data["country"], "Ukraine")
        self.assertEqual(expected_data["language"], "Ukrainian, English")
        self.assertEqual(expected_data["votes"], 296)
        self.assertEqual(expected_data["budget"], "$2000.000")
        self.assertEqual(expected_data["reviews"], 15.0)
        self.assertEqual(expected_data["date_published"], "2020-11-05")

    def test_get_ordering_by_date(self):
        
        """
        date_published is one of order by options.
        """

        # GIVEN
        self.mocks.create_movies()
        
        # WHEN
        response = self.client.get(MOVIES_SET_URL + "?ordering=-date_published")
        
        # THEN
        data = response.data
        expected_data = data["results"][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 5)
        self.assertEqual(expected_data["imdb_id"], "tt9055630")
        self.assertEqual(expected_data["title"], "H0us3")
        self.assertEqual(expected_data["original_title"], "H0us3")
        self.assertEqual(expected_data["year"], "2018")
        self.assertEqual(expected_data["genre"], "Horror, Sci-Fi, Thriller")
        self.assertEqual(expected_data["duration"], "105")
        self.assertEqual(expected_data["country"], "Spain")
        self.assertEqual(expected_data["language"], "Spanish")
        self.assertEqual(expected_data["votes"], 436)
        self.assertEqual(expected_data["budget"], "$700.000")
        self.assertEqual(expected_data["reviews"], 7.0)
        self.assertEqual(expected_data["date_published"], "2021-06-05")

    def test_post_request(self):
        
        """
        post_data is a new movie that will be created.
        """

        # GIVEN
        post_data = {
            "imdb_id": "tt4532038",
            "title": "Nonno questa volta è guerra",
            "original_title": "The War with Grandpa",
            "year": "2020",
            "genre": "Comedy, Drama, Family",
            "duration": "94",
            "country": "USA",
            "language": "English",
            "votes": 1377,
            "budget": "$100.000",
            "reviews": 40.0,
            "date_published": "2020-10-09"
        }

        # WHEN
        response = self.client.post(MOVIES_SET_URL, post_data)

        # THEN
        expected_data = response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(expected_data["imdb_id"], post_data["imdb_id"])
        self.assertEqual(expected_data["title"], post_data["title"])
        self.assertEqual(expected_data["original_title"], post_data["original_title"])
        self.assertEqual(expected_data["year"], post_data["year"])
        self.assertEqual(expected_data["genre"], post_data["genre"])
        self.assertEqual(expected_data["duration"], post_data["duration"])
        self.assertEqual(expected_data["country"], post_data["country"])
        self.assertEqual(expected_data["language"], post_data["language"])
        self.assertEqual(expected_data["votes"], post_data["votes"])
        self.assertEqual(expected_data["budget"], post_data["budget"])
        self.assertEqual(expected_data["reviews"], post_data["reviews"])
        self.assertEqual(expected_data["date_published"], post_data["date_published"])

    def test_put_request(self):
        
        """
        put_data is a know movie that will be updated.
        """

        # GIVEN
        id_movie = self.mocks.create_movies()

        put_data = {
            "imdb_id": "tt4532039",
            "title": "Avangers",
            "original_title": "Avangers",
            "year": "2019",
            "genre": "Comedy, Drama, Family",
            "duration": "94",
            "country": "USA",
            "language": "English",
            "votes": 1377,
            "budget": "$100.000",
            "reviews": 40.0,
            "date_published": "2020-10-09"
        }
        
        # WHEN
        response = self.client.put(MOVIES_SET_URL + str(id_movie["id"]) + "/",
                                   put_data, content_type='application/json')
        expected_data = response.data
        
        # THEN
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_data["imdb_id"], put_data["imdb_id"])
        self.assertEqual(expected_data["title"], put_data["title"])
        self.assertEqual(expected_data["original_title"], put_data["original_title"])
        self.assertEqual(expected_data["year"], put_data["year"])
        self.assertEqual(expected_data["genre"], put_data["genre"])
        self.assertEqual(expected_data["duration"], put_data["duration"])
        self.assertEqual(expected_data["country"], put_data["country"])
        self.assertEqual(expected_data["language"], put_data["language"])
        self.assertEqual(expected_data["votes"], put_data["votes"])
        self.assertEqual(expected_data["budget"], put_data["budget"])
        self.assertEqual(expected_data["reviews"], put_data["reviews"])
        self.assertEqual(expected_data["date_published"], put_data["date_published"])

    def test_delete_request(self):
        
        """
        id_movie is a know movie that will be deleted.
        """
        
        # GIVEN
        id_movie = self.mocks.create_movies()
            
        # WHEN 
        response = self.client.delete(MOVIES_SET_URL + str(id_movie["id"]) + "/")
        
        # THEN
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # WHEN
        response = self.client.get(MOVIES_SET_URL + str(id_movie["id"]) + "/")
        
        # THEN
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)