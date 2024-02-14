import requests

# Chamada de API sem autenticação para o site https://jsonplaceholder.typicode.com/posts

# GET

response = requests.get('https://jsonplaceholder.typicode.com/posts')

print("GET", response.status_code)

# print(response.json())

# POST

response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    data = {'title':'foo', 'body':'bar', 'userId':1}
)

print("POST", response.status_code)

# print(response.json())

# PUT

response = requests.put(
    'https://jsonplaceholder.typicode.com/posts/1',
    data = {'title':'foo', 'body':'bar', 'userId':1}
)

print("PUT", response.status_code)

# print(response.json())

# DELETE

response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')

print("DELETE", response.status_code)

# print(response.json())


# Chamada de API para o site http://www.omdbapi.com/ usando apikey e título do filme

response = requests.get('http://www.omdbapi.com/?apikey=68c858d7&t=back to the future')

print(response.status_code)

print(response.json())


# Chamada de API para o site https://geocode.maps.co/search?q=555+5th+Ave+New+York+NY+10017+US&api_key=api_key

api_key = '65c3e42a1ba9e761698287tbg28a5a8'

url = 'https://geocode.maps.co/search?q={nome_do_lugar}&api_key={api_key}'

nome_do_lugar = "Laranjeiras do Sul, Paraná, Brasil"

response = requests.get(url.format(nome_do_lugar=nome_do_lugar, api_key=api_key))

print(response.status_code)

# print(response.json())

# Chamada de API para o site https://api.openweathermap.org

api_key = '6fb849316852c21d7964a8a6564e9079'

url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br'

lat = '-25.407320'
lon = '-52.415013'

response = requests.get(url.format(lat=lat, lon=lon, api_key=api_key))

print(response.status_code)

print(response.json())

# Chamada de API para o site https://api.openweathermap.org para previsão do tempo

api_key = '6fb849316852c21d7964a8a6564e9079'

url = 'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br'

lat = '-25.407320'
lon = '-52.415013'

response = requests.get(url.format(lat=lat, lon=lon, api_key=api_key))

print(response.status_code)

print(response.json())