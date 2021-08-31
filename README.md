# IMDB Movies api

A Django API that will serve data from imdb movies csv. 

# How to run 

1. Clone the repository and create a python3 venv (I'm using 3.8.10)  
2. Run the command pip install -r requirements.txt 
3. Run the command python manage.py runserver 

# Tips 

There is a command to import the movies.csv. Command : python manage.py load_movies_csv   
To run the automated tests, you can use : ./manage.py test 

# How to use 

After run the api you will be able to access the endpoints movies/ and documentation/    

Accesing documentarion you will see this : 

![Captura de tela de 2021-08-31 00-01-59](https://user-images.githubusercontent.com/7093470/131434828-12b4f4d9-7580-41cb-8241-a7604e468689.png)


On movies you will be able to get the list of movies on pages of 1000 rows. The table has 85855 rows, so it would not be a good idea to bring all them at once.    
You can filter by the values of : imdb_id, title, genre, duration, country, language, date_published    

Example : http://127.0.0.1:8000/movies/?search=Maciste 

You can also order by the columns : date_published, reviews, votes 

Example : http://127.0.0.1:8000/movies/?ordering=reviews 

Fee free to combine the filters and use the others CRUD options as well  

Source :  https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset

