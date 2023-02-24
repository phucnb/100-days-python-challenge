import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

soup  = BeautifulSoup(html.text, 'html.parser')
movies = soup.find_all(name='div', class_='listicle-item')
movies_list = []
for movie in movies[1:]:
    movie_name = movie.find(name='img', class_='loading').get('alt')
    movies_list.append(f"{100 - movies.index(movie)}) {movie_name}")

with open('movies.txt', 'a') as file:
    for movie in reversed(movies_list):
        file.write(movie)
        file.write('\n')