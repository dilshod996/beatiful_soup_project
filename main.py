from bs4 import BeautifulSoup
import requests
webpage_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=webpage_url)
web_doc = response.text
soup = BeautifulSoup(web_doc, "html.parser")
all_movies = []
get_movie = soup.find_all(name="h3", class_="title")
for text in get_movie:
    text_name = text.getText()
    all_movies.append(text_name)
# movie names on the list
print(all_movies)
with open("movies.txt", "w") as file:
    for movie in all_movies:
        file.write(movie +"\n")
file.close()

