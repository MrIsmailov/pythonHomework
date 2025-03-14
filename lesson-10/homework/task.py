import requests
import random

# Task 1: Weather API

def get_weather(city):
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geocoding_response = requests.get(geocoding_url)
    if geocoding_response.status_code == 200:
        geocoding_data = geocoding_response.json()
        if geocoding_data['results']:
            latitude = geocoding_data['results'][0]['latitude']
            longitude = geocoding_data['results'][0]['longitude']
        else:
            print(f"City '{city}' not found.")
            return
    else:
        print(f"Failed to get geocoding data for {city}. Error code: {geocoding_response.status_code}")
        return

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    weather_response = requests.get(weather_url)
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        current_weather = weather_data['current_weather']
        print(f"Weather in {city}:")
        print(f"Temperature: {current_weather['temperature']}°C")
        print(f"Wind Speed: {current_weather['windspeed']} km/h")
        print(f"Weather: {current_weather['weathercode']}")
    else:
        print(f"Failed to get weather data for {city}. Error code: {weather_response.status_code}")

# Example 
get_weather("Tashkent")

# Task 2: 

def get_genre_id(genre_name, api_key):
    base_url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        "api_key": api_key,
        "language": "en-US"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        genres = response.json()["genres"]
        for genre in genres:
            if genre["name"].lower() == genre_name.lower():
                return genre["id"]
    return None

def get_random_movie(genre_id, api_key):
    base_url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": api_key,
        "with_genres": genre_id,
        "sort_by": "popularity.desc"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        movies = response.json()["results"]
        if movies:
            movie = random.choice(movies)
            print(f"Recommended Movie: {movie['title']}")
            print(f"Overview: {movie['overview']}")
        else:
            print("No movies found for this genre.")
    else:
        print(f"Failed to get movies. Error code: {response.status_code}")

# Example 
api_key = "your_tmdb_api_key"  
genre_name = input("Enter a movie genre: ")
genre_id = get_genre_id(genre_name, api_key)
if genre_id:
    get_random_movie(genre_id, api_key)
else:
    print(f"Genre '{genre_name}' not found.")