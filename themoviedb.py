# Anahtar kelimeye göre arama
# Vizyondaki film listesi
# tv top rated

import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "d6ba8b84fd87a2d57a068b87064c999c"

    # En popüler film listesi
    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

    def getTopRated(self):
        response = requests.get(f"{self.api_url}/tv/top_rated?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

movieApi = theMovieDb()

while True:
    secim = input("1- Popular Movies\n2- Search Movies\n3- Tv Top Rated\n4- Exit\nSeçim: ")

    if secim == "4":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])

        elif secim == "2":
            kw = input("Please enter your keyword for search: ")
            movies = movieApi.getSearchResults(kw)
            for movie in movies['results']:
                print(movie['name'])

        elif secim == "3":
            tvs = movieApi.getTopRated()
            for tv in tvs['results']:
                print(tv['name'])
