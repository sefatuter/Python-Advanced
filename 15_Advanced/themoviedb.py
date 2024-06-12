# themoviedb.org => film ve dizi arşivi
# themoviedb'nin sunduğu apiyi uygulamada kullan.
# Anahtar kelimeye göre arama.
# En popüler film listesi
# Vizyondaki film listesi


import requests
import json

class theMovieDb:
    def __init__(self) -> None:
        self.api_search = "https://api.themoviedb.org/3/search/keyword"
        self.api_popular = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
        self.api_key = "e79f361068bf5f70620904c952b5c4ce"
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNzlmMzYxMDY4YmY1ZjcwNjIwOTA0Yzk1MmI1YzRjZSIsInN1YiI6IjY2MmU4OGZiMDNiZjg0MDEyNWVhZTU1ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NpIRHrvmTZhwUk4sgWCRMQcq6HPmqBkloRfVotSrOOA"
        }

    def getPopulars(self):
        response = requests.get(self.api_popular, headers=self.headers)
        return response.json()

    def getSearchResults(self, keyword):
        response = requests.get(self.api_search + "?query=" + keyword + "&page=1", headers=self.headers)
        return response.json()
    
movieApi = theMovieDb()    

while True:
    secim = input('1- Popular Movies\n2- Search Movie\n3- Exit\nChoose: ')
    
    if secim == '3':
        break
    else:
        if secim == '1':
            movies = movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie['original_title'])
        
        elif secim == '2':
            keyword = input('Enter movie name: ')
            movies = movieApi.getSearchResults(keyword)
            for movie in movies["results"]:
                print(movie['name'])